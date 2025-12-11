import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

# ===============================
# Genel stil ayarları
# ===============================
plt.rcParams.update({
    'font.family': 'Times New Roman',
    'font.size': 12,
    'axes.titlesize': 14,
    'axes.labelsize': 12,
    'legend.fontsize': 10,
    'xtick.labelsize': 11,
    'ytick.labelsize': 11,
    'axes.grid': True,
    'grid.linestyle': '--',
    'grid.alpha': 0.3,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'lines.linewidth': 2.2,
})

# ===============================
# Dosya ve klasör ayarları
# ===============================
os.makedirs('figures', exist_ok=True)
scenario_files = {
    'S1': 's1_senaryo.csv',
    'S2': 's2_senaryo_antalya_2019-07-21.csv'
}

USD_to_TL = 41.6
EF_dg = 0.8  # kg CO2/kWh
C_pv = 0.02
C_wind = 0.015
C_dg = 0.25
C_bch = 0.002
C_bde = 0.003
carbon_price = 0.1  # $/kg CO2

MIN_SOC = 20
MAX_SOC = 90
BAT_CAPACITY = 500  # kWh

colors = {
    'PV': '#FFB74D',
    'WT': '#64B5F6',
    'DG': '#E57373',
    'B_ch': '#4DB6AC',
    'B_de': '#FFD54F',
    'Carbon': '#757575',
    'SOC_fill': '#C8E6C9',
    'SOC_line': '#388E3C'
}

# ===============================
# Senaryo bazlı grafikler
# ===============================
for s_name, file in scenario_files.items():
    df = pd.read_csv(file)
    hours = len(df)
    df['hour_label'] = [f"{h:02d}:00-{h+1:02d}:00" for h in range(hours)]

    df['total_load'] = df['served_h'] + df['served_s'] + df['served_c']
    df['total_gen'] = df['PV'] + df['WT'] + df['DG'] + df['p_bde'] - df['p_bch']
    df['renewable_eff'] = (df['PV'] + df['WT']) / (df['total_load'] + 1e-6) * 100
    df['emissions'] = df['DG'] * EF_dg

    # ===============================
    # 1 - Yenilenebilir Enerji Kullanımı
    # ===============================
    plt.figure(figsize=(12, 6))
    plt.plot(df['hour_label'], df['renewable_eff'].clip(0, 100),
             marker='o', color='#43A047', linewidth=2,
             label='Yenilenebilir Kullanım (%)')

    overproduction = (df['renewable_eff'] - 100).clip(lower=0)
    plt.bar(df['hour_label'], overproduction,
            color='red', alpha=0.5, label='Fazla Üretim')

    plt.title("Yenilenebilir Enerji Kullanımı")
    plt.xlabel('Zaman Aralığı')
    plt.ylabel('Yenilenebilir Kullanım (%)')
    plt.xticks(rotation=45)
    plt.ylim(0, max(110, df['renewable_eff'].max() * 1.2))

    plt.legend(loc='upper right')
    plt.tight_layout()
    plt.savefig(f'figures/{s_name}_renewable_efficiency.png', dpi=600)
    plt.close()

    # ===============================
    # 2 - Sistem Enerji Akışı ve Kaynak Katkısı
    # ===============================
    plt.figure(figsize=(12,6))
    plt.stackplot(df['hour_label'], df['PV'], df['WT'], df['DG'], df['p_bde'],
                  labels=['PV', 'Rüzgar', 'DG', 'Batarya Deşarj'],
                  colors=[colors['PV'], colors['WT'], colors['DG'], colors['B_de']], alpha=0.85)

    plt.plot(df['hour_label'], df['total_load'], color='k', marker='o',
             linewidth=3, label='Toplam Yük')

    plt.title("Sistem Enerji Akışı ve Kaynak Katkısı")
    plt.xlabel('Zaman Aralığı')
    plt.ylabel('Güç (kW)')
    plt.xticks(rotation=45)

    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.savefig(f'figures/{s_name}_total_gen_load.png', dpi=600)
    plt.close()

    # ===============================
    # 3 - Batarya Doluluk Oranı (SOC)
    # ===============================
    plt.figure(figsize=(12,6))
    E_b_percent = df['E_b'] / BAT_CAPACITY * 100

    plt.fill_between(df['hour_label'], MIN_SOC, MAX_SOC,
                     color=colors['SOC_fill'], alpha=0.35)

    plt.plot(df['hour_label'], E_b_percent, color=colors['SOC_line'],
             marker='o', linewidth=3, label='SOC (%)')

    plt.axhline(MIN_SOC, color='red', linestyle='--', label=f'Min SOC')
    plt.axhline(MAX_SOC, color='green', linestyle='--', label=f'Max SOC')

    plt.title("Batarya Doluluk Oranı (SOC)")
    plt.xlabel('Zaman Aralığı')
    plt.ylabel('SOC (%)')
    plt.xticks(rotation=45)
    plt.legend(loc='upper right')
    plt.tight_layout()
    plt.savefig(f'figures/{s_name}_battery_SOC.png', dpi=600)
    plt.close()

    # ===============================
    # 4 - Batarya Güç Akışı
    # ===============================
    plt.figure(figsize=(12,6))
    plt.bar(df['hour_label'], df['p_bch'], color=colors['B_ch'], alpha=0.75, label='Şarj')
    plt.bar(df['hour_label'], -df['p_bde'], color=colors['B_de'], alpha=0.75, label='Deşarj')

    plt.title("Batarya Güç Akışı")
    plt.xlabel('Zaman Aralığı')
    plt.ylabel('Güç (kW)')
    plt.xticks(rotation=45)

    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.savefig(f'figures/{s_name}_battery_power.png', dpi=600)
    plt.close()

    # ===============================
    # 5 - Karbon Emisyonu
    # ===============================
    plt.figure(figsize=(12,6))
    plt.bar(df['hour_label'], df['emissions'],
            color=colors['Carbon'], alpha=0.85, label='Emisyon')

    plt.title("Karbon Emisyonu")
    plt.xlabel('Zaman Aralığı')
    plt.ylabel('Emisyon (kg CO₂)')
    plt.xticks(rotation=45)

    plt.legend(loc='upper right')
    plt.tight_layout()
    plt.savefig(f'figures/{s_name}_carbon_emissions.png', dpi=600)
    plt.close()

    # ===============================
    # 6 - Toplam İşletme Maliyeti
    # ===============================
    from matplotlib.patches import Patch

    costs_usd = {
        'PV': df['PV'].sum() * C_pv,
        'WT': df['WT'].sum() * C_wind,
        'DG': df['DG'].sum() * C_dg,
        'Batarya Şarj': df['p_bch'].sum() * C_bch,
        'Batarya Deşarj': df['p_bde'].sum() * C_bde
    }

    emission_cost_usd = df['DG'].sum() * EF_dg * carbon_price
    total_cost_usd = sum(costs_usd.values())
    total_cost_tl = total_cost_usd * USD_to_TL
    emission_cost_tl = emission_cost_usd * USD_to_TL

    label_colors = {
        'PV': colors['PV'],
        'WT': colors['WT'],
        'DG': colors['DG'],
        'Batarya Şarj': colors['B_ch'],
        'Batarya Deşarj': colors['B_de'],
        'Karbon Emisyon': colors['Carbon']
    }

    fig, ax = plt.subplots(figsize=(12, 6))

    labels = list(costs_usd.keys())
    values = [costs_usd[lbl] for lbl in labels]
    bar_colors = [label_colors[lbl] for lbl in labels]

    bars = ax.bar(labels, values, color=bar_colors, alpha=0.85)

    ax.bar('Karbon Emisyon', emission_cost_usd, color=label_colors['Karbon Emisyon'], alpha=0.85)

    for bar, key in zip(bars, labels):
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height + total_cost_usd * 0.01,
            f"{height:.2f} $ / {height * USD_to_TL:.0f} TL",
            ha='center', va='bottom', fontsize=12
        )

    ax.text(
        len(labels),
        emission_cost_usd + total_cost_usd * 0.01,
        f"{emission_cost_usd:.2f}$ / {emission_cost_tl:.0f} TL",
        ha='center', va='bottom', fontsize=12
    )

    plt.title("Toplam İşletme Maliyeti")

    ax.text(
        0.98, 0.95,
        f"Toplam: {total_cost_usd:.2f} $ / {total_cost_tl:.0f} TL\n(Karbon emisyonu hariç)",
        ha='right', va='top',
        transform=ax.transAxes,
        fontsize=11,
        bbox=dict(facecolor='white', edgecolor='none', alpha=0.6)
    )

    ax.set_ylabel('Maliyet ($)')

    legend_patches = [
        Patch(facecolor=label_colors[lbl], label=lbl) for lbl in labels
    ]
    legend_patches.append(Patch(facecolor=label_colors['Karbon Emisyon'], label='Karbon Emisyon'))

    ax.legend(handles=legend_patches, loc='upper left', ncol=2)

    plt.tight_layout()
    plt.savefig(f'figures/{s_name}_daily_operating_costs.png', dpi=600)
    plt.close()

    # ===============================
    # 7 - Konut Yükü Kaynak Dağılımı
    # ===============================
    plt.figure(figsize=(12, 6))
    bottom_vals = pd.Series(0, index=df.index)

    for src in ['PV', 'WT', 'DG']:
        contrib = df[src].clip(upper=df['served_c'])
        plt.bar(df['hour_label'], contrib, bottom=bottom_vals,
                color=colors[src], alpha=0.85, label=src)
        bottom_vals += contrib

    plt.plot(df['hour_label'], df['served_c'], color='k',
             marker='o', linewidth=3, label='Toplam Konut Yük')

    plt.title("Konut Yükü Kaynak Dağılımı")
    plt.xlabel('Zaman Aralığı')
    plt.ylabel('Konut Yükü (kW)')
    plt.xticks(rotation=45)

    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.savefig(f'figures/{s_name}_residential_source.png', dpi=600)
    plt.close()

print("Tüm grafikler kaydedildi.")

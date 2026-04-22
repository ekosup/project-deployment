import random
import time
from datetime import date, timedelta

import pandas as pd
import streamlit as st


@st.cache_data
def generate_dummy_kpi_data(n_rows: int = 220) -> pd.DataFrame:
    random.seed(42)
    units = ["DJP", "DJBC", "DJPb", "DJKN", "BPPK", "Itjen"]
    layanan = ["SPT Tahunan", "NPWP", "Billing", "Lelang", "Perbendaharaan", "Konsultasi"]

    rows = []
    start_date = date.today() - timedelta(days=90)
    for i in range(n_rows):
        rows.append(
            {
                "tanggal": start_date + timedelta(days=random.randint(0, 90)),
                "unit": random.choice(units),
                "layanan": random.choice(layanan),
                "jumlah_permohonan": random.randint(50, 600),
                "success_rate": round(random.uniform(0.72, 0.99), 2),
                "rata_menit": random.randint(4, 90),
                "skor_kepuasan": round(random.uniform(3.2, 4.9), 2),
                "petugas_aktif": random.randint(5, 60),
                "batch_id": f"B-{1000 + i}",
            }
        )

    return pd.DataFrame(rows).sort_values("tanggal")


@st.cache_data
def slow_aggregate(data: pd.DataFrame, by_col: str) -> pd.DataFrame:
    time.sleep(1.4)
    return (
        data.groupby(by_col, as_index=False)
        .agg(
            total_permohonan=("jumlah_permohonan", "sum"),
            rata_success_rate=("success_rate", "mean"),
            rata_skor=("skor_kepuasan", "mean"),
        )
        .sort_values("total_permohonan", ascending=False)
    )

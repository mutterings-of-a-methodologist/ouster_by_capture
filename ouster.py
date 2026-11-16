#####################
# Ouster by Capture 
# Streamlit app for modeling a dictator AI transparency pact game
#####################
# This app was AI generated to model a dictator AI transparency pact game and 
# explore strategic interactions between different types of challengers and 
# the ruling coalition.

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

st.set_page_config(
    page_title="Ouster by Capture",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
        .block-container {
            padding-top: 2.35rem;
            padding-bottom: 0.35rem;
            padding-left: 1.6rem;
            padding-right: 1.6rem;
        }
        .paper-title {
            font-size: 2.05rem;
            font-weight: 800;
            line-height: 1.15;
            color: #0f172a;
            margin: 0 0 0.15rem 0;
        }
        .paper-question {
            font-size: 1.25rem;
            font-weight: 600;
            line-height: 1.25;
            color: #334155;
            margin: 0 0 0.55rem 0;
        }
        .section-label {
            font-size: 1.05rem;
            font-weight: 700;
            color: #0f172a;
            margin: 0 0 0.25rem 0;
        }
        .kpi-card {
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            border-radius: 8px;
            padding: 0.45rem 0.65rem;
            margin-bottom: 0.45rem;
        }
        .kpi-title {
            font-size: 0.84rem;
            font-weight: 700;
            color: #1e293b;
            margin: 0;
        }
        .kpi-val {
            font-size: 1.35rem;
            font-weight: 800;
            color: #0f172a;
            line-height: 1.2;
            margin: 0.05rem 0;
        }
        .kpi-sub {
            font-size: 0.74rem;
            line-height: 1.25;
            color: #475569;
            margin: 0;
        }
        div[data-testid="stAlert"] {
            padding: 0.45rem 0.65rem;
            margin-top: 0.2rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

PRESETS = {
    "Entrenched Autocracy (China / Russia)": {
        "S": 0.25, "W": 0.04, "g": 8.5, "x": 1.0,
        "omega": 0.78, "p": 0.35, "delta": 0.85, "kappa": 0.65,
    },
    "Nascent Autocracy": {
        "S": 0.12, "W": 0.03, "g": 5.5, "x": 0.5,
        "omega": 0.85, "p": 0.25, "delta": 0.45, "kappa": 0.25,
    },
    "Established Democracy": {
        "S": 0.95, "W": 0.50, "g": 0.2, "x": 8.5,
        "omega": 0.30, "p": 0.75, "delta": 0.80, "kappa": 0.85,
    },
    "Nascent Democracy": {
        "S": 0.85, "W": 0.45, "g": 2.2, "x": 5.5,
        "omega": 0.52, "p": 0.50, "delta": 0.60, "kappa": 0.45,
    },
}

CHALLENGERS = {
    "(a) Domestic Insider (Inner-Circle Coup)": {
        "key": "a",
        "col_player": "Domestic Insider (Winning Coalition Elite)",
        "col_0": "C1: Stay Loyal\n(Keep Leader)",
        "col_1": "C2: Stage Coup\n(Oust Leader)",
        "desc": "Inner-circle elites decide whether to stay loyal or exploit unguarded AI tools to seize power.",
    },
    "(b) Foreign Outsider (External Rival / Sponsor)": {
        "key": "b",
        "col_player": "Foreign Outsider (Rival State / Sponsor)",
        "col_0": "C1: Hold Back\n(Keep Leader)",
        "col_1": "C2: Back Subversion\n(Oust Leader)",
        "desc": "A foreign power decides whether to hold back or use frontier AI subversion to topple the incumbent.",
    },
    "(c) The People (Mass Uprising)": {
        "key": "c",
        "col_player": "The People (Citizens / Dissidents)",
        "col_0": "C1: Acquiesce\n(Keep Leader)",
        "col_1": "C2: Mobilize Revolt\n(Oust Leader)",
        "desc": "Citizens weigh regime surveillance/public goods against AI-enabled coordination to revolt.",
    },
    "(d) Autonomous AI ('Country of Geniuses in a Datacenter')": {
        "key": "d",
        "col_player": "Autonomous AI ('Country of Geniuses in a Datacenter')",
        "col_0": "C1: Remain Aligned\n(Keep Leader)",
        "col_1": "C2: Override Rule\n(Oust Leader)",
        "desc": "An unguarded frontier AI cluster crosses an autonomy threshold and displaces human leadership directly.",
    },
}

if "preset_name" not in st.session_state:
    st.session_state.preset_name = "Entrenched Autocracy (China / Russia)"
    for k, v in PRESETS[st.session_state.preset_name].items():
        st.session_state[k] = v


def apply_preset():
    chosen = st.session_state.preset_selector
    st.session_state.preset_name = chosen
    for k, v in PRESETS[chosen].items():
        st.session_state[k] = v


def compute_model(S, W, g, x, omega_0, p, delta, kappa, challenger_key):
    W = min(W, S)
    loyalty = W / S

    omega_1 = 0.20 * omega_0
    A_0 = 0.60 + 0.40 * omega_0
    A_1 = 0.45 + 0.15 * omega_1
    kappa_1 = min(1.0, kappa + 0.15)
    kappa_0 = max(0.0, kappa - 0.10)

    def hazards(A, om, kap):
        ha = np.clip(0.04 + 0.18 * om + 0.10 * A + 0.012 * g - 0.10 * kap, 0.01, 0.90)
        hb = np.clip(0.03 + 0.14 * om + 0.10 * A + 0.08 * (1 - S) - 0.08 * kap, 0.01, 0.90)
        hc = np.clip(0.03 + 0.12 * A + 0.09 * om - 0.010 * g - 0.05 * kap, 0.01, 0.90)
        hd = np.clip(0.02 + 0.24 * (A * om) + 0.12 * om - 0.12 * kap, 0.01, 0.90)
        pi_keep = (1 - ha) * (1 - hb) * (1 - hc) * (1 - hd)
        return {"a": ha, "b": hb, "c": hc, "d": hd, "keep": pi_keep, "oust": 1.0 - pi_keep}

    haz_1 = hazards(A_1, omega_1, kappa_1)
    haz_0 = hazards(A_0, omega_0, kappa_0)

    b_race, penalty = 2.0, 5.5
    net_race_bonus = (1.0 - delta) * b_race - delta * p * penalty

    UL_1_keep = round(0.85 * (x + g) + 0.15 * (0.85 * x + 0.80 * g) - 0.25, 2)
    UL_1_oust = round(x + g * loyalty - 0.50 * omega_1, 2)

    UL_0_keep = round(0.70 * (x + g) + 0.30 * (0.85 * x + 0.80 * g) + net_race_bonus, 2)
    UL_0_oust = round(x + g * loyalty - 0.50 * omega_0 - 0.5 * delta * p * penalty, 2)

    h_pace = haz_1[challenger_key]
    h_race = haz_0[challenger_key]

    if challenger_key == "a":
        UC_1_keep = round(0.45 * g + 0.30 * x, 2)
        UC_1_oust = round((1.0 - loyalty) * g * (0.35 + h_pace) - 2.2 * kappa_1, 2)
        UC_0_keep = round(0.40 * g + 0.25 * x, 2)
        UC_0_oust = round((1.0 - loyalty) * g * (0.45 + h_race) - 1.5 * kappa_0 + 1.2 * omega_0, 2)
    elif challenger_key == "b":
        UC_1_keep = round(1.50, 2)
        UC_1_oust = round(4.5 * h_pace + 1.5 * (1.0 - S) - 2.0 * kappa_1, 2)
        UC_0_keep = round(1.00, 2)
        UC_0_oust = round(5.5 * h_race + 2.0 * (1.0 - S) + 1.5 * omega_0 - 1.5 * kappa_0, 2)
    elif challenger_key == "c":
        UC_1_keep = round(0.55 * x, 2)
        UC_1_oust = round(0.65 * x * (0.4 + h_pace) + 2.5 * h_pace - 0.25 * g, 2)
        UC_0_keep = round(0.45 * x, 2)
        UC_0_oust = round(0.65 * x * (0.5 + h_race) + 3.0 * h_race - 0.20 * g, 2)
    else:
        UC_1_keep = round(1.20 * (1.0 - omega_1), 2)
        UC_1_oust = round(6.5 * h_pace + 2.0 * omega_1 - 2.8 * kappa_1, 2)
        UC_0_keep = round(0.80 * (1.0 - omega_0), 2)
        UC_0_oust = round(7.5 * h_race + 3.2 * omega_0 - 2.0 * kappa_0, 2)

    UL = np.array([[UL_1_keep, UL_1_oust], [UL_0_keep, UL_0_oust]])
    UC = np.array([[UC_1_keep, UC_1_oust], [UC_0_keep, UC_0_oust]])

    nash_cells = []
    for r in range(2):
        for c in range(2):
            if UL[r, c] >= UL[1 - r, c] and UC[r, c] >= UC[r, 1 - c]:
                nash_cells.append((r, c))

    V_1 = UL_1_oust + haz_1["keep"] * (UL_1_keep - UL_1_oust)
    V_0 = UL_0_oust + haz_0["keep"] * (UL_0_keep - UL_0_oust)

    num = b_race + (haz_0["keep"] * (UL_0_keep - UL_0_oust) - haz_1["keep"] * (UL_1_keep - UL_1_oust))
    delta_star_raw = num / max(b_race + p * penalty, 1e-6)
    p_star_raw = (num - delta * b_race) / max(delta * penalty, 1e-6)
    delta_star = np.clip(delta_star_raw, 0.0, 1.0)
    p_star = np.clip(p_star_raw, 0.0, 1.0)

    return {
        "loyalty": loyalty, "haz_1": haz_1, "haz_0": haz_0,
        "UL": UL, "UC": UC, "nash_cells": nash_cells,
        "V_1": V_1, "V_0": V_0, "delta_star": delta_star, "p_star": p_star,
        "delta_star_raw": delta_star_raw, "p_star_raw": p_star_raw,
        "dU_1": UL_1_keep - UL_1_oust, "dU_0": UL_0_keep - UL_0_oust,
    }


def fmt_threshold(raw):
    """Show thresholds honestly: values above 1 mean no feasible value sustains compliance."""
    if raw > 1.0:
        return "> 1.00"
    return f"{max(raw, 0.0):.2f}"


with st.sidebar:
    st.header("1. Regime Type")
    st.selectbox(
        "Choose a Political System",
        list(PRESETS.keys()),
        index=list(PRESETS.keys()).index(st.session_state.preset_name),
        key="preset_selector",
        on_change=apply_preset,
    )

    st.header("2. Who Threatens the Leader?")
    challenger_label = st.selectbox(
        "Select Column Player (Ouster Actor)",
        list(CHALLENGERS.keys()),
        index=0,
    )
    challenger_info = CHALLENGERS[challenger_label]
    st.caption(challenger_info["desc"])

    st.divider()
    st.header("3. Selectorate & Coalition")
    S = st.slider(
        "Selectorate Size (S) — Share of society with a formal say in picking the leader (voters in a democracy; party/elite pool in a dictatorship)",
        0.05, 1.00, step=0.01, key="S",
    )
    W = st.slider(
        "Winning Coalition (W) — Essential backers the leader must satisfy to stay in office (majority of voters vs. tiny inner circle)",
        0.01, float(S), step=0.01, key="W",
    )
    g = st.slider(
        "Private Rents (g) — Exclusive perks, money, and patronage paid only to inner-circle backers (high in dictatorships, near zero in democracies)",
        0.0, 10.0, step=0.1, key="g",
    )
    x = st.slider(
        "Public Goods (x) — Broad benefits shared by everyone (economic growth, stability, public services)",
        0.0, 10.0, step=0.1, key="x",
    )

    st.divider()
    st.header("4. AI Risk & Enforcement")
    omega = st.slider(
        "AI Opaqueness (Ω) — How hidden and unguarded frontier AI systems are (higher = easier for insiders or rogue AI to turn against the ruler)",
        0.05, 1.00, step=0.01, key="omega",
    )
    p = st.slider(
        "Detection Probability (p) — Chance that secret AI racing or treaty cheating gets caught",
        0.00, 1.00, step=0.01, key="p",
    )
    delta = st.slider(
        "Discount Factor (δ) — Short- vs. long-term tradeoff (0 = desperate for immediate gains; 1 = prioritizes long-term survival)",
        0.05, 0.99, step=0.01, key="delta",
    )
    kappa = st.slider(
        "State Oversight Capacity (κ) — Ability of the government to monitor and control its own AI labs and security forces",
        0.00, 1.00, step=0.01, key="kappa",
    )

res = compute_model(S, W, g, x, omega, p, delta, kappa, challenger_info["key"])

# Visible Title + Question
st.markdown(
    """
    <div class="paper-title">Ouster by Capture</div>
    <div class="paper-question">Does AI Pacing and Transparency Advantage Authoritarian Survival?</div>
    """,
    unsafe_allow_html=True,
)

st.caption(
    "The app starts from illustrative regime presets so the mechanism is visible; every parameter can be changed "
    "with the sliders. Results are conditional model outputs, not empirical estimates. See the accompanying brief."
)

# ---------------------------------------------------------
# Middle Row: 2x2 Game Matrix (Left) + Thresholds & Equilibrium (Right)
# ---------------------------------------------------------
game_col, stats_col = st.columns([3.35, 1.15])

with game_col:
    st.markdown(
        f"<div class='section-label'>2×2 Strategic-Form Game: Incumbent Leader vs. {challenger_info['col_player']}</div>",
        unsafe_allow_html=True,
    )
    fig_m, ax_m = plt.subplots(figsize=(9.6, 3.35))
    ax_m.set_xlim(0, 11.8)
    ax_m.set_ylim(0, 4.75)
    ax_m.axis("off")

    ax_m.text(7.35, 4.52, f"Column Player: {challenger_info['col_player']}",
              ha="center", va="center", fontsize=10, fontweight="bold", color="#0f172a")
    ax_m.text(5.20, 4.02, challenger_info["col_0"],
              ha="center", va="center", fontsize=9, fontweight="bold", color="#1e293b")
    ax_m.text(9.50, 4.02, challenger_info["col_1"],
              ha="center", va="center", fontsize=9, fontweight="bold", color="#1e293b")

    ax_m.text(0.32, 1.95, "Row Player:\nIncumbent Leader",
              ha="center", va="center", fontsize=9.5, fontweight="bold", color="#0f172a", rotation=90)

    row_labels = [
        f"Row 1: Join Pacing\n& Transparency (τ = 1)\n[Ω₁ = {0.2*omega:.2f}]",
        f"Row 2: Covert AI Race\n/ Defect (τ = 0)\n[Ω₀ = {omega:.2f}]",
    ]
    row_y = [2.82, 1.08]
    col_x = [5.20, 9.50]

    outcomes_text = [
        ["Status Quo Preserved\n(Leader Kept; AI Paced)", "Ouster Attempt Under Pacing\n(Leader Removed; AI Audited)"],
        ["Covert Race Continues\n(Leader Kept; High AI Risk)", "Unguarded AI Coup / Takeover\n(Leader Removed; Opaque AI)"],
    ]

    for r in range(2):
        ax_m.text(1.90, row_y[r], row_labels[r], ha="center", va="center", fontsize=8.8, fontweight="bold", color="#1e293b")
        for c in range(2):
            is_nash = (r, c) in res["nash_cells"]
            if is_nash and c == 0:
                fc, ec, lw = "#dcfce7", "#15803d", 2.5
            elif is_nash and c == 1:
                fc, ec, lw = "#fee2e2", "#b91c1c", 2.5
            else:
                fc, ec, lw = "#f8fafc", "#cbd5e1", 1.1

            box = FancyBboxPatch(
                (col_x[c] - 1.92, row_y[r] - 0.68), 3.84, 1.36,
                boxstyle="round,pad=0.04", fc=fc, ec=ec, lw=lw
            )
            ax_m.add_patch(box)

            ul_val = res["UL"][r, c]
            uc_val = res["UC"][r, c]
            badge = "★ NASH EQUILIBRIUM" if is_nash else ("Outcome: Leader Kept" if c == 0 else "Outcome: Leader Ousted")
            badge_color = "#15803d" if (is_nash and c == 0) else ("#b91c1c" if (is_nash and c == 1) else "#64748b")

            ax_m.text(col_x[c], row_y[r] + 0.44, badge, ha="center", va="center",
                      fontsize=8.3, fontweight="bold", color=badge_color)
            ax_m.text(col_x[c], row_y[r] + 0.05, outcomes_text[r][c], ha="center", va="center",
                      fontsize=8.3, color="#334155")
            ax_m.text(col_x[c], row_y[r] - 0.40, f"Payoffs: (Leader = {ul_val:.2f}, Challenger = {uc_val:.2f})",
                      ha="center", va="center", fontsize=8.8, fontweight="bold", color="#0f172a")

    plt.tight_layout(pad=0.15)
    st.pyplot(fig_m, use_container_width=True)

with stats_col:
    st.markdown("<div class='section-label'>Key Thresholds</div>", unsafe_allow_html=True)
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-title">Survival Boost (ΔΠ_keep)</div>
            <div class="kpi-val">{(res['haz_1']['keep'] - res['haz_0']['keep'])*100:+.1f} pp</div>
            <div class="kpi-sub">Gain in survival odds from joining pacing vs. racing.</div>
        </div>
        <div class="kpi-card">
            <div class="kpi-title">Discount Factor (δ*)</div>
            <div class="kpi-val">{fmt_threshold(res['delta_star_raw'])}</div>
            <div class="kpi-sub">Min. long-term weight vs. short-term gain to comply (current δ = {delta:.2f}); "&gt; 1.00" = compliance cannot be sustained.</div>
        </div>
        <div class="kpi-card">
            <div class="kpi-title">Detection Probability (p*)</div>
            <div class="kpi-val">{fmt_threshold(res['p_star_raw'])}</div>
            <div class="kpi-sub">Min. inspection chance to deter cheating; 0.00 = self-enforcing (current p = {p:.2f}).</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if res["nash_cells"]:
        eq_labels = []
        for r_eq, c_eq in res["nash_cells"]:
            strat_l = "Join Pacing (τ=1)" if r_eq == 0 else "Covert Race (τ=0)"
            strat_c = "Keep Leader" if c_eq == 0 else "Oust Leader"
            eq_labels.append(f"{strat_l} / {strat_c}")
        st.info(
            f"**Pure-strategy Nash Eq:** {'; '.join(eq_labels)}  \n"
            f"**Expected Utility:** V(τ=1) = **{res['V_1']:.2f}** vs. V(τ=0) = **{res['V_0']:.2f}**"
        )
    else:
        st.info(
            f"**No pure-strategy equilibrium** in this 2×2  \n"
            f"**Expected Utility:** V(τ=1) = **{res['V_1']:.2f}** vs. V(τ=0) = **{res['V_0']:.2f}**"
        )

    v_pref = 0 if res["V_1"] >= res["V_0"] else 1
    if res["nash_cells"] and all(r != v_pref for r, _ in res["nash_cells"]):
        st.caption(
            "Note: the 2×2 equilibrium holds the challenger's action fixed, while V averages over all four "
            "removal risks, so the two can point in different directions."
        )
    if res["dU_1"] <= 0 or res["dU_0"] <= 0:
        st.caption(
            "Note: here the leader's payoff from being ousted is at least as high as from staying (public goods "
            "are shared by everyone), so V mainly reflects payoff levels, not survival odds."
        )

# ---------------------------------------------------------
# Bottom Row: 4 Ouster Channels & Opaqueness Curve
# ---------------------------------------------------------
col1, col2 = st.columns(2)
with col1:
    st.markdown("<div class='section-label'>All 4 Removal Risks Compared (Π_oust Breakdown)</div>", unsafe_allow_html=True)
    labels = [
        "(a) Domestic Insider\n(Elites hijack unguarded AI)",
        "(b) Foreign Outsider\n(Rival state backs challenger)",
        "(c) The People\n(Citizens coordinate uprising)",
        "(d) Autonomous AI\n('Country of geniuses in a datacenter' acts alone)",
    ]
    h1 = [res["haz_1"][k] * 100 for k in ["a", "b", "c", "d"]]
    h0 = [res["haz_0"][k] * 100 for k in ["a", "b", "c", "d"]]
    fig1, ax1 = plt.subplots(figsize=(5.8, 2.15))
    y = np.arange(len(labels))
    ax1.barh(y - 0.18, h1, 0.35, label="Join Pacing (τ = 1)", color="#15803d")
    ax1.barh(y + 0.18, h0, 0.35, label="Covert Race (τ = 0)", color="#b91c1c")
    ax1.set_yticks(y)
    ax1.set_yticklabels(labels, fontsize=8.3)
    ax1.invert_yaxis()
    ax1.set_xlabel("Removal Risk by Channel (%)", fontsize=8.5)
    ax1.tick_params(axis="x", labelsize=8)
    ax1.legend(fontsize=7.8, loc="lower right")
    ax1.grid(axis="x", linestyle="--", alpha=0.35)
    plt.tight_layout(pad=0.2)
    st.pyplot(fig1, use_container_width=True)

with col2:
    st.markdown("<div class='section-label'>How AI Opaqueness (Ω) Shifts Expected Leader Utility V(τ)</div>", unsafe_allow_html=True)
    omegas = np.linspace(0.05, 1.0, 40)
    v1s, v0s = [], []
    for om in omegas:
        o = compute_model(S, W, g, x, om, p, delta, kappa, challenger_info["key"])
        v1s.append(o["V_1"])
        v0s.append(o["V_0"])
    fig2, ax2 = plt.subplots(figsize=(5.8, 2.15))
    ax2.plot(omegas, v1s, label="V(τ = 1): Expected Utility under Pacing", color="#15803d", lw=2.2)
    ax2.plot(omegas, v0s, label="V(τ = 0): Expected Utility under Covert Race", color="#b91c1c", lw=2.2, ls="--")
    ax2.axvline(omega, color="#334155", ls=":", lw=1.3, label=f"Current Opaqueness Ω = {omega:.2f}")
    ax2.set_xlabel("AI Capability Opaqueness (Ω: 0 = Fully Audited, 1 = Hidden)", fontsize=8.5)
    ax2.set_ylabel("Expected Leader Utility V(τ)", fontsize=8.5)
    ax2.tick_params(axis="both", labelsize=8)
    ax2.legend(fontsize=7.8)
    ax2.grid(True, linestyle="--", alpha=0.35)
    plt.tight_layout(pad=0.2)
    st.pyplot(fig2, use_container_width=True)
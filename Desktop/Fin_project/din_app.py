import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.subheader(
    "Динамика изменений реальной и номинальной начисленной заработной плате работников организаций по трем видам экономической деятельности в Российской Федерации за 2000-2023 гг."
)
df = pd.read_excel("C:\\Users\\sour\\Downloads\\fin_zpl_2023.xlsx")
df_inf = pd.read_excel("C:\\Users\\sour\\Downloads\\inflation.xlsx")
is_clicked = st.button("Использованные данные")
if is_clicked:
    st.dataframe(df)
    st.dataframe(df_inf)

y = pd.Series(df.loc[int(0)][df.columns[1:].astype(int)])
x = df.columns[1:].astype(int)


def calculate_inf(a, b):
    c = []
    for i in a:
        for k in b:
            if a.index(i) == b.index(k):
                c.append(i * (1 - (k / 100)))
    return c


sal_data = list(pd.Series(df.loc[int(0)][df.columns[1:].astype(int)]))
salb_data = list(pd.Series(df.loc[int(1)][df.columns[1:].astype(int)]))
salh_data = list(pd.Series(df.loc[int(2)][df.columns[1:].astype(int)]))
inf_data = list(df_inf["Всего"].astype(float))
inf = inf_data[::-1]

# first graph
fig_1 = plt.figure()
plt.plot(x, y, marker=".", label="Номинальная ЗП")
plt.plot(x, calculate_inf(sal_data, inf), "r", marker=".", label="Реальная ЗП")
plt.legend()
plt.title(
    "Динамика номинальной среднемесячной ЗП работников в сфере образования РФ за 2000-2023 гг"
)
plt.xlabel("Год")
plt.ylabel("Средняя зарплата")
st.pyplot(fig_1)

# second graph
y_1 = pd.Series(df.loc[int(1)][df.columns[1:].astype(int)])
fig_2 = plt.figure()
plt.plot(x, y_1, marker=".", label="Номинальная ЗП")
plt.plot(x, calculate_inf(salb_data, inf), "r", marker=".", label="Реальная ЗП")
plt.legend()
plt.title(
    "Динамика номинальной среднемесячной ЗП работников в сфере строительства РФ за 2000-2023 гг"
)
plt.xlabel("Год")
plt.ylabel("Средняя зарплата")
st.pyplot(fig_2)

# third graph
y_2 = pd.Series(df.loc[int(2)][df.columns[1:].astype(int)])
fig_3 = plt.figure()
plt.plot(x, y_2, marker=".", label="Номинальная ЗП")
plt.plot(x, calculate_inf(salh_data, inf), "r", marker=".", label="Реальная ЗП")
plt.legend()
plt.title(
    "Динамика номинальной среднемесячной ЗП работников в сфере гостиничного и ресторанного бизнеса РФ за 2000-2023 гг"
)
plt.xlabel("Год")
plt.ylabel("Средняя зарплата")
st.pyplot(fig_3)

st.write(
    "**Вывод**: В рассмотренных сферах реальная зарплата растет медленнее номинальной зарплаты в связи с тем, что уровень инфляции растет быстрее номинальной зарплаты"
)



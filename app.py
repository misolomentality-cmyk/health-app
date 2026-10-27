
import streamlit as st

st.set_page_config(
    page_title="Ты болеешь?",
    page_icon="❤️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Оформлення для телефонів
st.markdown("""
<style>
    .block-container {
        max-width: 500px;
        padding: 1.5rem 1rem 2rem;
    }

    h1, h2, p {
        text-align: center;
    }

    div.stButton > button {
        width: 100%;
        min-height: 48px;
        border-radius: 12px;
        font-size: 18px;
    }

    [data-testid="stImage"] img {
        width: 100%;
        height: auto;
        border-radius: 14px;
    }

    [data-testid="stSidebar"] {
        display: none;
    }
</style>
""", unsafe_allow_html=True)


# Стан сторінки
if "page" not in st.session_state:
    st.session_state.page = 0


def next_page():
    st.session_state.page += 1


def restart():
    st.session_state.page = 0


# Головний екран
if st.session_state.page == 0:
    st.image("previu.jpg", use_container_width=True)

    st.title("Ты болеешь?")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Да 🥺", use_container_width=True):
            st.session_state.page = 1
            st.rerun()

    with col2:
        if st.button("Нет 😊", use_container_width=True):
            st.session_state.page = 5
            st.rerun()


# Перша картинка
elif st.session_state.page == 1:
    st.image("kotik.jpg", use_container_width=True)
    st.write("У кошечки болит")

    st.button(
        "Далее →",
        on_click=next_page,
        use_container_width=True
    )


# Друга картинка
elif st.session_state.page == 2:
    st.image("pesik.jpg", use_container_width=True)
    st.write("У собачки болит")

    st.button(
        "Далее →",
        on_click=next_page,
        use_container_width=True
    )


# Третя картинка
elif st.session_state.page == 3:
    st.image("smail.jpg", use_container_width=True)
    st.write("У Вікусі пусть не болит")

    st.button(
        "Далее →",
        on_click=next_page,
        use_container_width=True
    )

elif st.session_state.page == 4:
    st.image("litvin.png", use_container_width=True)



# Відповідь на «Нет»
elif st.session_state.page == 6:
    st.title("Хорошо ❤️")
    st.write("Тут буде твій текст для відповіді «Нет».")

    st.button(
        "Назад",
        on_click=restart,
        use_container_width=True
    )

import streamlit as st
from streamlit_elements import Elements

st.set_page_config(
    page_title="Material-UI Button Designer",
    page_icon="🕹️",
)

st.image(
    "https://emojipedia-us.s3.amazonaws.com/source/skype/289/joystick_1f579-fe0f.png",
    width=125,
)
st.title("Material-UI Button Designer")

st.write(
    "Design your Material-UI buttons, add clickable hyperlinks, integrate them in your Streamlit apps! 🎈"
)
st.write("")

with st.form(key="my_form_2"):
    col1, col2 = st.columns(2)
    with col1:
        btn_name = st.text_input(
            "🅰️ Button label", value="Press me!", help="Add a label to your button."
        )
        buttonStyle = st.selectbox(
            "🕹️ Button style",
            ["outlined", "contained", "link"],
            1,
            help="Select the button style.",
        )
        color = st.selectbox(
            "🎨 Button color",
            ["primary", "secondary", "default"],
            1,
            help="Select the button color.",
        )

    with col2:
        hrefLink = st.text_input(
            "🔗 Hyperlink", "https://streamlit.io/", help="Add a link to your button."
        )
        size = st.selectbox(
            "📦 Button size",
            ["small", "medium", "large"],
            1,
            help="Select the button size.",
        )
        icon_selected = st.selectbox(
            "📸 Icon",
            ["no icon", "send", "delete", "save", "chat", "call", "accessible"],
            index=1,
            help="Select the button icon (more to come!)",
        )

        def get_icon(mt, icon):

            if icon == "send":
                return mt.icons.send, "mt.icons.send"
            elif icon == "delete":
                return mt.icons.delete, "mt.icons.delete"
            elif icon == "save":
                return mt.icons.save, "mt.icons.save"
            elif icon == "chat":
                return mt.icons.chat, "mt.icons.chat"
            elif icon == "call":
                return mt.icons.call, "mt.icons.call"
            elif icon == "accessible":
                return mt.icons.accessible, "mt.icons.accessible"

        st.write("")

    st.form_submit_button("Create your button!")

mt = Elements()
start_icon = get_icon(mt, icon_selected)

st.subheader("Button")

mt.button(
    btn_name,
    target="_blank",
    size=size,
    variant=buttonStyle,
    color=color,
    start_icon=start_icon[0],
    href=hrefLink,
)
mt.show("zero")

st.subheader("Code")

st.write(
    f"""

First, pip install streamlit-elements

```python
pip install streamlit-elements
```

Second, add the following code to your Streamlit app

```python
import streamlit as st
from streamlit_elements import Elements

mt = Elements()
mt.button(\
"{btn_name}", \
target="_blank", \
size="{size}", \
variant="{buttonStyle}", \
color="{color}", \
start_icon="{start_icon[1]}", \
href="{hrefLink}")
```
"""
)

import streamlit as st
import random
from streamlit_elements import Elements

st.set_page_config(
    page_title="Material UI Button Designer",
    page_icon="🕹️",
)

st.image(
    "https://emojipedia-us.s3.amazonaws.com/source/skype/289/joystick_1f579-fe0f.png",
    width=125,
)
st.title("Material UI Button Designer")

st.markdown(
    "Design your [Material UI buttons](https://mui.com/components/buttons/), add hyperlinks, integrate them in your Streamlit apps!"
)

st.write("")

with st.form(key="my_form_2"):
    cs, col1, col2, cf = st.columns([0.05, 1, 1, 0.05])
    with col1:
        bg = st.color_picker(
            "🎨 Background Color",
            "#FF4B4B",
            help="Select the background color. Only works with the `contained` button style. You can choose between `HEX`, `RGB` or `HSL`.",
        )
        label = st.text_input(
            "🅰️ Button label",
            value="I am a button!",
            help="Add a label to your button.",
        )

        buttonStyle = st.selectbox(
            "🕹️ Button style",
            ["contained", "outlined"],
            1,
            help="Select the button style.",
        )

        onclick = st.selectbox(
            "🖱️ App rerun on click",
            ["none", "rerun"],
            index=1,
            help="If 'rerun' is selected, your button will rerun your app and send state and storage values to Streamlit each time it is clicked",
        )

    with col2:
        fg = st.color_picker(
            "🎨 Font Color",
            "#FFFFFF",
            help="Pick a font color. Only works with the `contained` button style. You can choose between `HEX`, `RGB` or `HSL`.",
        )
        size = st.selectbox(
            "📦 Button size",
            ["small", "medium", "large"],
            1,
            help="Select the button size.",
        )

        icon_selected = st.selectbox(
            "📸 Icon",
            [
                "accessible",
                "add box",
                "alarm",
                "arrow back",
                "arrow downward",
                "arrow forward",
                "arrow upward",
                "call",
                "chat",
                "delete",
                "save",
                "send",
            ],
            index=1,
            help="Select an icon for your button (more to come!). You can get the full list of icons here: https://mui.com/components/material-icons/)",
        )

        hrefLink = st.text_input(
            "🔗 Hyperlink",
            "https://mui.com/components/buttons/",
            help="Add a link to your button.",
        )

        def get_onclick(mt, onclick):

            if onclick == "rerun":
                return mt.rerun, "mt.rerun"
            elif onclick == "none":
                return "", '"none"'

        st.write("")

        # These icons are available in the Material-UI icons library. You can find them here: https://mui.com/components/material-icons/

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
            elif icon == "alarm":
                return mt.icons.access_alarm, "mt.icons.access_alarm"
            elif icon == "accessible":
                return mt.icons.accessible, "mt.icons.accessible"
            elif icon == "add box":
                return mt.icons.add_box, "mt.icons.add_box"
            elif icon == "arrow upward":
                return mt.icons.arrow_upward, "mt.icons.arrow_upward"
            elif icon == "arrow downward":
                return mt.icons.arrow_downward, "mt.icons.arrow_downward"
            elif icon == "arrow back":
                return mt.icons.arrow_back, "mt.icons.arrow_back"
            elif icon == "arrow forward":
                return mt.icons.arrow_forward, "mt.icons.arrow_forward"

        st.write("")

    st.form_submit_button("Create your button!")

mt = Elements()
start_icon = get_icon(mt, icon_selected)
onclick_behaviour = get_onclick(mt, onclick)

st.subheader("Here's your button:")

cs, col1, col2, cf = st.columns([0.05, 0.6, 2, 0.05])
with col1:
    st.image("arrow.png", width=150)
with col2:

    if buttonStyle == "outlined":
        mt.button(
            label,
            target="_blank",
            size=size,
            variant=buttonStyle,
            color="secondary",
            on_click=onclick_behaviour[0],
            start_icon=start_icon[0],
            href=hrefLink,
        )

    elif buttonStyle == "contained":
        mt.button(
            label,
            target="_blank",
            size=size,
            variant=buttonStyle,
            style={"color": fg, "background": bg},
            on_click=onclick_behaviour[0],
            start_icon=start_icon[0],
            href=hrefLink,
        )

    st.title("")
    st.subheader("")
    st.write("")
    mt.show("button")

st.subheader("Your button's code:")

if buttonStyle == "contained":
    st.write(
        f"""

    First, you need to install the awesome ```streamlit-elements``` component by [@okld](https://github.com/okld):

    ```python
    pip install streamlit-elements
    ```

    Second, add the following code to your Streamlit app:

    ```python
    import streamlit as st
    from streamlit_elements import Elements

    mt = Elements()
    \n\
    mt.button(\n\
    "{label}", \n\
    target="_blank", \n\
    size="{size}", \n\
    variant="{buttonStyle}", \n\
    start_icon={start_icon[1]}, \n\
    onclick={onclick_behaviour[1]}, \n\
    style={{"color":"{fg}", "background":"{bg}"}}, \n\
    href="{hrefLink}")\n\

    mt.show("{random.randint(0, 1000)}")

    ```

    Voilà! 🤗

    """
    )

elif buttonStyle == "outlined":
    st.write(
        f"""

    First, you need to install the awesome ```streamlit-elements``` component by [@okld](https://github.com/okld):

    ```python
    pip install streamlit-elements
    ```

    Second, add the following code to your Streamlit app:

    ```python
    import streamlit as st
    from streamlit_elements import Elements

    mt = Elements()
    \n\
    mt.button(\n\
    "{label}", \n\
    target="_blank", \n\
    size="{size}", \n\
    variant="{buttonStyle}", \n\
    start_icon={start_icon[1]}, \n\
    onclick={onclick_behaviour[1]}, \n\
    color="secondary", \n\
    href="{hrefLink}")\n\

    mt.show("{random.randint(0, 1000)}")

    ```

    Voilà! 🤗

    """
    )
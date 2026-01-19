
files = [
    "00ed3d5b-d738-4cce-aaff-231495bc9635.png",
    "1c9f660a-81a2-4099-ad29-eb89886ed9da.png",
    "1d04c6ce-5d10-45c6-bdc9-0525904e8ed8.png",
    "002ae8dc-39e5-4613-8bb6-c30bd036d989.png",
    "2bfdb4be-1bb5-4cf5-a918-fa06fad1c540.png",
    "2f37592c-ea04-48b1-a817-1dea1d61cb41.png",
    "2fdcb81e-b978-43f9-a9b0-0924dc799238.png",
    "4b0fbf90-59b0-40b1-b5e6-b260dda290a1.png",
    "6eff0b17-b4b1-4b9a-866e-13126fb40e2e.png",
    "62d5f2ee-47c1-4ec5-9fdf-7f87185a5dfb.png",
    "459abbb2-d4f2-425a-83a6-fc4330048c66.png",
    "584a668f-2a71-4342-8e69-caba10ccfba0.png",
    "978d29c5-c456-4fac-9806-41f0dec66dbe.png",
    "999ebeaa-4598-412e-acea-6030ec7190f4.png",
    "9024b0da-94d9-46da-be74-b9756d166e87.png",
    "9075ad13-1379-42f5-b3d9-6cfed847ea14.png",
    "506953b6-e387-4fff-ba88-2b9106155482.png",
    "b8db4c96-b622-4512-807d-eaa12a3cacce.png",
    "b69eedc6-0c6e-4670-b3ac-d8612b9ccde1.png",
    "c6bce7a7-298e-49c9-8a64-62f5f201ea81.png",
    "ca564822-7d5c-46f8-b975-03147ef89911.png",
    "ChatGPT Image Jan 18, 2026, 07_27_00 PM.png",
    "ChatGPT Image Jan 18, 2026, 07_32_59 PM.png",
    "ChatGPT Image Jan 18, 2026, 07_35_37 PM.png",
    "ChatGPT Image Jan 18, 2026, 07_38_29 PM.png",
    "ChatGPT Image Jan 18, 2026, 07_49_27 PM.png",
    "ChatGPT Image Jan 18, 2026, 07_51_45 PM.png",
    "ChatGPT Image Jan 18, 2026, 07_54_13 PM.png",
    "ChatGPT Image Jan 18, 2026, 08_02_30 PM - Edited.png",
    "ChatGPT Image Jan 18, 2026, 09_05_30 PM - Edited.png",
    "ChatGPT Image Jan 18, 2026, 09_07_34 PM - Edited.png",
    "ChatGPT Image Jan 18, 2026, 09_10_08 PM - Edited.png",
    "e0b9c70a-e855-4334-a51f-e4d4d3fe4f92.png",
    "e772e3f0-91ec-4573-9816-8e7b82a094fa.png",
    "ee006d1a-9909-47a8-90c4-5e0354c0ce3b.png"
]

base_path = "images/logosss/"

html_output = ""

for filename in files:
    alt_text = filename.rsplit('.', 1)[0]
    html_output += f"""                                  <div class="logo-item">
                                    <div class="image-wrapper anima-fade-in-bottom">
                                      <img alt="{alt_text}" class="lazyload"
                                        data-src="{base_path}{filename}"
                                        loading="lazy"
                                        src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsQAAA7EAZUrDhsAAAANSURBVBhXYzh8+PB/AAffA0nNPuCLAAAAAElFTkSuQmCC" />
                                    </div>
                                  </div>
"""

# Add the empty spacer divs
html_output += '                                  <div class="logo-item logo-item--empty tablet-only"></div>\n'
html_output += '                                  <div class="logo-item logo-item--empty tablet-only"></div>\n'
html_output += '                                  <div class="logo-item logo-item--empty mobile-only"></div>'

print(html_output)

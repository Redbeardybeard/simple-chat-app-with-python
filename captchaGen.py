from captcha.image import ImageCaptcha
from captcha.audio import AudioCaptcha
import random



def create_captcha():
    l1 = [chr(random.randint(65,90)) for x in range(5)]
    capthca_text = ''.join(map(str, l1))
    print(f"created captcha with: {capthca_text}")

    # creating image captcha
    image_captcha = ImageCaptcha()
    image = image_captcha.generate_image(capthca_text)
    image.save("captcha.png")
# image_captcha.write(capthca_text,"captcha.png")


# create audio captcha

# not working idky

# capthca_text = "1234"
# print(capthca_text)
# audio = AudioCaptcha()
# audio_data = audio.generate(capthca_text)
# audio_file = "captcha_"+capthca_text+".wav"
# audio.write(capthca_text,audio_file)



if __name__ == "__main__":
    create_captcha()

import logging
from PIL import Image
from io import BytesIO

# Set up logging
logger = logging.getLogger(__name__)


def resize_photo(update, context):
    # Check if t user sent a photo
    if not update.message.photo:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Please send a photo to cc.")
        return

    # Get t p file ft user's message
    photo_file = update.message.photo[-1].get_file()

    # Download t pf
    original_image_name = 'original_photo.jpg'
    photo_file.download(original_image_name)

    # Get t user's specified dimensions
    width = context.args[0]
    height = context.args[1]

    # cc - image from camera
    resized_image_name = 'resized' + original_image_name
    resized_photo = resize_photo_dimensions(original_image_name, width, height)
    resized_photo.save(resized_image_name)

    # Send t rf
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(resized_image_name, 'rb'))


def resize_photo_dimensions(photo_path, width, height):
    logger.info(f"Resizing photo {photo_path} to dimensions {width}x{height}")

    photo = Image.open(photo_path)
    resized_photo = photo.resize((int(width), int(height)))

    return resized_photo



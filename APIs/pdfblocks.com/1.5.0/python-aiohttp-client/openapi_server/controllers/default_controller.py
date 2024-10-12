from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_password_v14_xx_response import AddPasswordV14XXResponse
from openapi_server import util


async def add_image_watermark_v1(request: web.Request, file, image, margin=None, transparency=None) -> web.Response:
    """Add an image watermark to a PDF

    Add an image watermark to each page of a PDF document.

    :param file: The input PDF document
    :type file: str
    :param image: The image to add as a watermark. The format of the image can be either PNG or JPEG.
    :type image: str
    :param margin: The distance in inches from the border of the page to the image watermark.
    :type margin: float
    :param transparency: The transparency level for the image watermark from 0 (opaque) to 100 (transparent).
    :type transparency: int

    """
    return web.Response(status=200)


async def add_password_v1(request: web.Request, file, password, encryption_algorithm=None) -> web.Response:
    """Add a password to a PDF

    Protect a PDF document with a password. Encrypt the PDF document to prevent unauthorized access.

    :param file: The input PDF document
    :type file: str
    :param password: The password required to open the file.
    :type password: str
    :param encryption_algorithm: The algorithm used to encrypt the PDF document.
    :type encryption_algorithm: str

    """
    return web.Response(status=200)


async def add_restrictions_v1(request: web.Request, file, owner_password, allow_accessibility=None, allow_assemble_document=None, allow_change_content=None, allow_comment_and_fill_form=None, allow_copy_content=None, allow_fill_form=None, allow_print=None, allow_print_high_resolution=None, encryption_algorithm=None, user_password=None) -> web.Response:
    """Add restrictions to a PDF

    Add restrictions to prevent copying, printing, and modifying a PDF document.

    :param file: The input PDF document
    :type file: str
    :param owner_password: The password required to open and change permissions of the PDF document.
    :type owner_password: str
    :param allow_accessibility: If false, accessibility programs can&#39;t read the text or images of the document.
    :type allow_accessibility: bool
    :param allow_assemble_document: If false, the user can&#39;t assemble or manipulate the document.
    :type allow_assemble_document: bool
    :param allow_change_content: If false, the user can&#39;t change the content of the document.
    :type allow_change_content: bool
    :param allow_comment_and_fill_form: If false, the user can&#39;t add, edit or modify annotations or fill form fields.
    :type allow_comment_and_fill_form: bool
    :param allow_copy_content: If false, the user can&#39;t copy text and images to the clipboard.
    :type allow_copy_content: bool
    :param allow_fill_form: If false, the user can&#39;t fill forms fields.
    :type allow_fill_form: bool
    :param allow_print: If false, the user can&#39;t print the document.
    :type allow_print: bool
    :param allow_print_high_resolution: If false, the user can&#39;t print the document in high resolution.
    :type allow_print_high_resolution: bool
    :param encryption_algorithm: The algorithm used to encrypt the PDF document.
    :type encryption_algorithm: str
    :param user_password: The password required to open the PDF document. If the &#x60;user_password&#x60; is not set, the user will be able to open the document without a password.
    :type user_password: str

    """
    return web.Response(status=200)


async def add_text_watermark_v1(request: web.Request, file, line_1, color=None, line_2=None, line_3=None, margin=None, template=None, transparency=None) -> web.Response:
    """Add a text watermark to a PDF

    Add a text watermark to each page of a PDF document. Choose from several watermark templates.

    :param file: The input PDF document
    :type file: str
    :param line_1: The first line of text of the watermark.
    :type line_1: str
    :param color: The color of the text watermark.
    :type color: str
    :param line_2: The second line of text of the watermark.
    :type line_2: str
    :param line_3: The third line of text of the watermark.
    :type line_3: str
    :param margin: The distance in inches from the border of the page to the text watermark.
    :type margin: float
    :param template: The [id of the text watermark template](https://www.pdfblocks.com/docs/api/v1/text-watermark-templates.pdf).
    :type template: int
    :param transparency: The transparency level for the text watermark from 0 (opaque) to 100 (transparent).
    :type transparency: int

    """
    return web.Response(status=200)


async def extract_pages_v1(request: web.Request, file, first_page=None, last_page=None) -> web.Response:
    """Extract pages from a PDF

    Extract one or more pages from a PDF document.

    :param file: The input PDF document
    :type file: str
    :param first_page: The first page of the range to extract. If empty, it defaults to the first page of the PDF document.
    :type first_page: int
    :param last_page: The last page of the range to extract. If empty, it defaults to the last page of the PDF document.
    :type last_page: int

    """
    return web.Response(status=200)


async def merge_documents_v1(request: web.Request, file=None) -> web.Response:
    """Merge PDF documents

    Combine multiple PDF documents into a single PDF document.

    :param file: The array of PDF documents. PDF documents will be merged in the same order they are inserted into this array.
    :type file: List[str]

    """
    return web.Response(status=200)


async def remove_pages_v1(request: web.Request, file, first_page=None, last_page=None) -> web.Response:
    """Remove pages from a PDF

    Remove one or more pages from a PDF document.

    :param file: The input PDF document
    :type file: str
    :param first_page: The first page of the range to remove from the PDF document. If empty, it defaults to the first page of the document.
    :type first_page: int
    :param last_page: The last page of the range to remove from the PDF document. If empty, it defaults to the last page of the document.
    :type last_page: int

    """
    return web.Response(status=200)


async def remove_password_v1(request: web.Request, file, password) -> web.Response:
    """Remove the password from a PDF

    Remove the password from an encrypted PDF document. The PDF document will no longer require a password to open.

    :param file: The input PDF document
    :type file: str
    :param password: The password required to open the file.
    :type password: str

    """
    return web.Response(status=200)


async def remove_restrictions_v1(request: web.Request, file) -> web.Response:
    """Remove the restrictions from a PDF

    Remove all the restrictions from a PDF document.

    :param file: The input PDF document
    :type file: str

    """
    return web.Response(status=200)


async def remove_signatures_v1(request: web.Request, file) -> web.Response:
    """Remove the signatures from a PDF

    Remove the cryptographic signatures and timestamps from a PDF document.

    :param file: The input PDF document
    :type file: str

    """
    return web.Response(status=200)


async def reverse_pages_v1(request: web.Request, file) -> web.Response:
    """Reverse the pages of a PDF

    Reverse the order of the pages of a PDF document.

    :param file: The input PDF document
    :type file: str

    """
    return web.Response(status=200)


async def rotate_pages_v1(request: web.Request, angle, file, first_page=None, last_page=None) -> web.Response:
    """Rotate pages in a PDF

    Rotate one or more pages in a PDF document.

    :param angle: The angle of rotation of the pages. Positive angles rotate the pages clockwise. Negative angles rotate the pages counter-clockwise.
    :type angle: int
    :param file: The input PDF document
    :type file: str
    :param first_page: The first page of the range to rotate in the PDF document. If empty, it defaults to the first page of the document.
    :type first_page: int
    :param last_page: The last page of the range to rotate in the PDF document. If empty, it defaults to the last page of the document.
    :type last_page: int

    """
    return web.Response(status=200)

# coding: utf-8

# import models into model package
from openapi_server.models.auto_data import AutoData
from openapi_server.models.auto_qr_code import AutoQRCode
from openapi_server.models.auto_qr_code_batch import AutoQRCodeBatch
from openapi_server.models.auto_qr_code_metadata import AutoQRCodeMetadata
from openapi_server.models.background_style import BackgroundStyle
from openapi_server.models.batch_format import BatchFormat
from openapi_server.models.batch_output_file import BatchOutputFile
from openapi_server.models.bcc import Bcc
from openapi_server.models.cc import Cc
from openapi_server.models.cell_phone import CellPhone
from openapi_server.models.color import Color
from openapi_server.models.contact_data import ContactData
from openapi_server.models.contact_qr_code import ContactQRCode
from openapi_server.models.contact_qr_code_metadata import ContactQRCodeMetadata
from openapi_server.models.crypto_payment_data import CryptoPaymentData
from openapi_server.models.crypto_payment_qr_code import CryptoPaymentQRCode
from openapi_server.models.crypto_payment_qr_code_metadata import CryptoPaymentQRCodeMetadata
from openapi_server.models.cryptocurrency import Cryptocurrency
from openapi_server.models.ec_level import ECLevel
from openapi_server.models.email import Email
from openapi_server.models.email_data import EmailData
from openapi_server.models.email_qr_code import EmailQRCode
from openapi_server.models.email_qr_code_metadata import EmailQRCodeMetadata
from openapi_server.models.embedded_image import EmbeddedImage
from openapi_server.models.embedded_image_multipart import EmbeddedImageMultipart
from openapi_server.models.fax import Fax
from openapi_server.models.format import Format
from openapi_server.models.generic_error import GenericError
from openapi_server.models.geolocation_data import GeolocationData
from openapi_server.models.geolocation_qr_code import GeolocationQRCode
from openapi_server.models.geolocation_qr_code_metadata import GeolocationQRCodeMetadata
from openapi_server.models.geolocation_uri_format import GeolocationUriFormat
from openapi_server.models.gradient import Gradient
from openapi_server.models.gradient_stop import GradientStop
from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.home_phone import HomePhone
from openapi_server.models.icon import Icon
from openapi_server.models.icons import Icons
from openapi_server.models.image_metadata import ImageMetadata
from openapi_server.models.image_multipart_body import ImageMultipartBody
from openapi_server.models.inner_eye_shapes import InnerEyeShapes
from openapi_server.models.inner_eye_style import InnerEyeStyle
from openapi_server.models.linear_gradient import LinearGradient
from openapi_server.models.location_inner import LocationInner
from openapi_server.models.me_card_data import MeCardData
from openapi_server.models.module_shapes import ModuleShapes
from openapi_server.models.module_style import ModuleStyle
from openapi_server.models.outer_eye_shapes import OuterEyeShapes
from openapi_server.models.outer_eye_style import OuterEyeStyle
from openapi_server.models.output_file import OutputFile
from openapi_server.models.phone import Phone
from openapi_server.models.phone_data import PhoneData
from openapi_server.models.phone_qr_code import PhoneQRCode
from openapi_server.models.phone_qr_code_metadata import PhoneQRCodeMetadata
from openapi_server.models.photo import Photo
from openapi_server.models.radial_gradient import RadialGradient
from openapi_server.models.sms_data import SMSData
from openapi_server.models.smsqr_code import SMSQRCode
from openapi_server.models.smsqr_code_metadata import SMSQRCodeMetadata
from openapi_server.models.size import Size
from openapi_server.models.size_multipart import SizeMultipart
from openapi_server.models.style import Style
from openapi_server.models.text_qr_code import TextQRCode
from openapi_server.models.text_qr_code_metadata import TextQRCodeMetadata
from openapi_server.models.title import Title
from openapi_server.models.to import To
from openapi_server.models.to1 import To1
from openapi_server.models.uri import URI
from openapi_server.models.url import Url
from openapi_server.models.v_card_data import VCardData
from openapi_server.models.validation_error import ValidationError
from openapi_server.models.videophone import Videophone
from openapi_server.models.wi_fi_data import WiFiData
from openapi_server.models.wi_fi_qr_code import WiFiQRCode
from openapi_server.models.wi_fi_qr_code_metadata import WiFiQRCodeMetadata
from openapi_server.models.wi_fi_security import WiFiSecurity
from openapi_server.models.work_phone import WorkPhone

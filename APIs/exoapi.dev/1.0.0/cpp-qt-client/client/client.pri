QT += network

HEADERS += \
# Models
    $${PWD}/OAIBarcode_generator_post_400_response.h \
    $${PWD}/OAIBarcode_generator_post_request.h \
    $${PWD}/OAIHtml_renderer_post_request.h \
    $${PWD}/OAIReverse_geocoding_get_200_response.h \
    $${PWD}/OAIUnit_converter_get_200_response.h \
# APIs
    $${PWD}/OAIBarcodeGeneratorApi.h \
    $${PWD}/OAIHTMLRendererApi.h \
    $${PWD}/OAIReverseGeocodingApi.h \
    $${PWD}/OAIUnitConverterApi.h \
# Others
    $${PWD}/OAIHelpers.h \
    $${PWD}/OAIHttpRequest.h \
    $${PWD}/OAIObject.h \
    $${PWD}/OAIEnum.h \
    $${PWD}/OAIHttpFileElement.h \
    $${PWD}/OAIServerConfiguration.h \
    $${PWD}/OAIServerVariable.h \
    $${PWD}/OAIOauth.h

SOURCES += \
# Models
    $${PWD}/OAIBarcode_generator_post_400_response.cpp \
    $${PWD}/OAIBarcode_generator_post_request.cpp \
    $${PWD}/OAIHtml_renderer_post_request.cpp \
    $${PWD}/OAIReverse_geocoding_get_200_response.cpp \
    $${PWD}/OAIUnit_converter_get_200_response.cpp \
# APIs
    $${PWD}/OAIBarcodeGeneratorApi.cpp \
    $${PWD}/OAIHTMLRendererApi.cpp \
    $${PWD}/OAIReverseGeocodingApi.cpp \
    $${PWD}/OAIUnitConverterApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp

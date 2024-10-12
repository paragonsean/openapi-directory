QT += network

HEADERS += \
# Models
    $${PWD}/OAIColorDto.h \
    $${PWD}/OAIErrorResponseDto.h \
    $${PWD}/OAIFoRequestDto.h \
    $${PWD}/OAIFoTransformRequestDto.h \
    $${PWD}/OAIFontDto.h \
    $${PWD}/OAIFontStyle.h \
    $${PWD}/OAIImageResponseDto.h \
    $${PWD}/OAIPdfConcatenationRequestDto.h \
    $${PWD}/OAIPdfMetadataDto.h \
    $${PWD}/OAIPdfResponseDto.h \
    $${PWD}/OAIPdfToImageOptions.h \
    $${PWD}/OAIPdfToImageRequestDto.h \
    $${PWD}/OAIPdfWriteStringOptions.h \
    $${PWD}/OAIPdfWriteStringRequestDto.h \
    $${PWD}/OAIWkHtmlToPdfRequestDto.h \
    $${PWD}/OAIXOriginPoint.h \
    $${PWD}/OAIYOriginPoint.h \
# APIs
    $${PWD}/OAIPdfApi.h \
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
    $${PWD}/OAIColorDto.cpp \
    $${PWD}/OAIErrorResponseDto.cpp \
    $${PWD}/OAIFoRequestDto.cpp \
    $${PWD}/OAIFoTransformRequestDto.cpp \
    $${PWD}/OAIFontDto.cpp \
    $${PWD}/OAIFontStyle.cpp \
    $${PWD}/OAIImageResponseDto.cpp \
    $${PWD}/OAIPdfConcatenationRequestDto.cpp \
    $${PWD}/OAIPdfMetadataDto.cpp \
    $${PWD}/OAIPdfResponseDto.cpp \
    $${PWD}/OAIPdfToImageOptions.cpp \
    $${PWD}/OAIPdfToImageRequestDto.cpp \
    $${PWD}/OAIPdfWriteStringOptions.cpp \
    $${PWD}/OAIPdfWriteStringRequestDto.cpp \
    $${PWD}/OAIWkHtmlToPdfRequestDto.cpp \
    $${PWD}/OAIXOriginPoint.cpp \
    $${PWD}/OAIYOriginPoint.cpp \
# APIs
    $${PWD}/OAIPdfApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp

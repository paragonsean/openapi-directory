QT += network

HEADERS += \
# Models
    $${PWD}/OAIValidationResult.h \
# APIs
    $${PWD}/OAIConversionApi.h \
    $${PWD}/OAIMetadataApi.h \
    $${PWD}/OAIValidationApi.h \
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
    $${PWD}/OAIValidationResult.cpp \
# APIs
    $${PWD}/OAIConversionApi.cpp \
    $${PWD}/OAIMetadataApi.cpp \
    $${PWD}/OAIValidationApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp

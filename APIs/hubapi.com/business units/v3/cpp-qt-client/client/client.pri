QT += network

HEADERS += \
# Models
    $${PWD}/OAICollectionResponsePublicBusinessUnitNoPaging.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIErrorDetail.h \
    $${PWD}/OAIPublicBusinessUnit.h \
    $${PWD}/OAIPublicBusinessUnitLogoMetadata.h \
# APIs
    $${PWD}/OAIBusinessUnitApi.h \
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
    $${PWD}/OAICollectionResponsePublicBusinessUnitNoPaging.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIErrorDetail.cpp \
    $${PWD}/OAIPublicBusinessUnit.cpp \
    $${PWD}/OAIPublicBusinessUnitLogoMetadata.cpp \
# APIs
    $${PWD}/OAIBusinessUnitApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp

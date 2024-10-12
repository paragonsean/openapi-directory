QT += network

HEADERS += \
# Models
    $${PWD}/OAISubResource.h \
    $${PWD}/OAITransformation.h \
    $${PWD}/OAITransformationProperties.h \
# APIs
    $${PWD}/OAITransformationsApi.h \
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
    $${PWD}/OAISubResource.cpp \
    $${PWD}/OAITransformation.cpp \
    $${PWD}/OAITransformationProperties.cpp \
# APIs
    $${PWD}/OAITransformationsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp

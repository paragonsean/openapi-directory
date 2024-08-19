QT += network

HEADERS += \
# Models
    $${PWD}/OAIActivation.h \
    $${PWD}/OAIActivationResource.h \
    $${PWD}/OAIActivationResourcesPage.h \
# APIs
    $${PWD}/OAIActivationsApi.h \
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
    $${PWD}/OAIActivation.cpp \
    $${PWD}/OAIActivationResource.cpp \
    $${PWD}/OAIActivationResourcesPage.cpp \
# APIs
    $${PWD}/OAIActivationsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp

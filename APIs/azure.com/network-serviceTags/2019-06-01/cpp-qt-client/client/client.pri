QT += network

HEADERS += \
# Models
    $${PWD}/OAIServiceTagInformation.h \
    $${PWD}/OAIServiceTagInformationPropertiesFormat.h \
    $${PWD}/OAIServiceTagsListResult.h \
# APIs
    $${PWD}/OAIDefaultApi.h \
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
    $${PWD}/OAIServiceTagInformation.cpp \
    $${PWD}/OAIServiceTagInformationPropertiesFormat.cpp \
    $${PWD}/OAIServiceTagsListResult.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp

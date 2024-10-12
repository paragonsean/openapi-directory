QT += network

HEADERS += \
# Models
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIOperationListResult.h \
    $${PWD}/OAIOperation_display.h \
    $${PWD}/OAIResourceLink.h \
    $${PWD}/OAIResourceLinkFilter.h \
    $${PWD}/OAIResourceLinkProperties.h \
    $${PWD}/OAIResourceLinkResult.h \
# APIs
    $${PWD}/OAIOperationsApi.h \
    $${PWD}/OAIResourceLinksApi.h \
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
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIOperationListResult.cpp \
    $${PWD}/OAIOperation_display.cpp \
    $${PWD}/OAIResourceLink.cpp \
    $${PWD}/OAIResourceLinkFilter.cpp \
    $${PWD}/OAIResourceLinkProperties.cpp \
    $${PWD}/OAIResourceLinkResult.cpp \
# APIs
    $${PWD}/OAIOperationsApi.cpp \
    $${PWD}/OAIResourceLinksApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp

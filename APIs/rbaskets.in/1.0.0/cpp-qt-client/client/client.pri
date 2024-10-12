QT += network

HEADERS += \
# Models
    $${PWD}/OAIBasketInfo.h \
    $${PWD}/OAIBaskets.h \
    $${PWD}/OAIConfig.h \
    $${PWD}/OAIRequest.h \
    $${PWD}/OAIRequests.h \
    $${PWD}/OAIResponse.h \
    $${PWD}/OAIServiceStats.h \
    $${PWD}/OAIToken.h \
    $${PWD}/OAIVersion.h \
# APIs
    $${PWD}/OAIBasketsApi.h \
    $${PWD}/OAIRequestsApi.h \
    $${PWD}/OAIResponsesApi.h \
    $${PWD}/OAIServiceApi.h \
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
    $${PWD}/OAIBasketInfo.cpp \
    $${PWD}/OAIBaskets.cpp \
    $${PWD}/OAIConfig.cpp \
    $${PWD}/OAIRequest.cpp \
    $${PWD}/OAIRequests.cpp \
    $${PWD}/OAIResponse.cpp \
    $${PWD}/OAIServiceStats.cpp \
    $${PWD}/OAIToken.cpp \
    $${PWD}/OAIVersion.cpp \
# APIs
    $${PWD}/OAIBasketsApi.cpp \
    $${PWD}/OAIRequestsApi.cpp \
    $${PWD}/OAIResponsesApi.cpp \
    $${PWD}/OAIServiceApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp

QT += network

HEADERS += \
# Models
    $${PWD}/OAIBindtoanothersku_request.h \
    $${PWD}/OAIGetSKUseller_200_response.h \
    $${PWD}/OAIGetallbySellerId_200_response_inner.h \
    $${PWD}/OAIGetbySkuId_200_response_inner.h \
    $${PWD}/OAIGetpagedadmin_200_response.h \
    $${PWD}/OAIInsertSKUBinding_request.h \
# APIs
    $${PWD}/OAISKUBindingsApi.h \
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
    $${PWD}/OAIBindtoanothersku_request.cpp \
    $${PWD}/OAIGetSKUseller_200_response.cpp \
    $${PWD}/OAIGetallbySellerId_200_response_inner.cpp \
    $${PWD}/OAIGetbySkuId_200_response_inner.cpp \
    $${PWD}/OAIGetpagedadmin_200_response.cpp \
    $${PWD}/OAIInsertSKUBinding_request.cpp \
# APIs
    $${PWD}/OAISKUBindingsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp

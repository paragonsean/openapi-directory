QT += network

HEADERS += \
# Models
    $${PWD}/OAIAddress.h \
    $${PWD}/OAIAssignTerminalsRequest.h \
    $${PWD}/OAIAssignTerminalsResponse.h \
    $${PWD}/OAIFindTerminalRequest.h \
    $${PWD}/OAIFindTerminalResponse.h \
    $${PWD}/OAIGetStoresUnderAccountRequest.h \
    $${PWD}/OAIGetStoresUnderAccountResponse.h \
    $${PWD}/OAIGetTerminalDetailsRequest.h \
    $${PWD}/OAIGetTerminalDetailsResponse.h \
    $${PWD}/OAIGetTerminalsUnderAccountRequest.h \
    $${PWD}/OAIGetTerminalsUnderAccountResponse.h \
    $${PWD}/OAIMerchantAccount.h \
    $${PWD}/OAIServiceError.h \
    $${PWD}/OAIStore.h \
# APIs
    $${PWD}/OAIGeneralApi.h \
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
    $${PWD}/OAIAddress.cpp \
    $${PWD}/OAIAssignTerminalsRequest.cpp \
    $${PWD}/OAIAssignTerminalsResponse.cpp \
    $${PWD}/OAIFindTerminalRequest.cpp \
    $${PWD}/OAIFindTerminalResponse.cpp \
    $${PWD}/OAIGetStoresUnderAccountRequest.cpp \
    $${PWD}/OAIGetStoresUnderAccountResponse.cpp \
    $${PWD}/OAIGetTerminalDetailsRequest.cpp \
    $${PWD}/OAIGetTerminalDetailsResponse.cpp \
    $${PWD}/OAIGetTerminalsUnderAccountRequest.cpp \
    $${PWD}/OAIGetTerminalsUnderAccountResponse.cpp \
    $${PWD}/OAIMerchantAccount.cpp \
    $${PWD}/OAIServiceError.cpp \
    $${PWD}/OAIStore.cpp \
# APIs
    $${PWD}/OAIGeneralApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp

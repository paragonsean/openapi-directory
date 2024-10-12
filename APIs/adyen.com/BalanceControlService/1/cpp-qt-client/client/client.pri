QT += network

HEADERS += \
# Models
    $${PWD}/OAIAmount.h \
    $${PWD}/OAIBalanceTransferRequest.h \
    $${PWD}/OAIBalanceTransferResponse.h \
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
    $${PWD}/OAIAmount.cpp \
    $${PWD}/OAIBalanceTransferRequest.cpp \
    $${PWD}/OAIBalanceTransferResponse.cpp \
# APIs
    $${PWD}/OAIGeneralApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp

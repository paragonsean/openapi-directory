QT += network

HEADERS += \
# Models
    $${PWD}/OAIBiddingFunction.h \
    $${PWD}/OAIListBiddingFunctionsResponse.h \
# APIs
    $${PWD}/OAIBiddersApi.h \
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
    $${PWD}/OAIBiddingFunction.cpp \
    $${PWD}/OAIListBiddingFunctionsResponse.cpp \
# APIs
    $${PWD}/OAIBiddersApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp

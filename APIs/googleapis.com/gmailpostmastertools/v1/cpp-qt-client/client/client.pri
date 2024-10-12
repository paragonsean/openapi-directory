QT += network

HEADERS += \
# Models
    $${PWD}/OAIDeliveryError.h \
    $${PWD}/OAIDomain.h \
    $${PWD}/OAIFeedbackLoop.h \
    $${PWD}/OAIIpReputation.h \
    $${PWD}/OAIListDomainsResponse.h \
    $${PWD}/OAIListTrafficStatsResponse.h \
    $${PWD}/OAITrafficStats.h \
# APIs
    $${PWD}/OAIDomainsApi.h \
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
    $${PWD}/OAIDeliveryError.cpp \
    $${PWD}/OAIDomain.cpp \
    $${PWD}/OAIFeedbackLoop.cpp \
    $${PWD}/OAIIpReputation.cpp \
    $${PWD}/OAIListDomainsResponse.cpp \
    $${PWD}/OAIListTrafficStatsResponse.cpp \
    $${PWD}/OAITrafficStats.cpp \
# APIs
    $${PWD}/OAIDomainsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp

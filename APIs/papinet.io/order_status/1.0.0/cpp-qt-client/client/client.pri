QT += network

HEADERS += \
# Models
    $${PWD}/OAIListOfOrders.h \
    $${PWD}/OAIOrder.h \
    $${PWD}/OAIOrderHeader.h \
    $${PWD}/OAIOrderLineItem.h \
    $${PWD}/OAIOrderLineItem_quantities_inner.h \
    $${PWD}/OAIPaginationLinks.h \
    $${PWD}/OAIPaginationLinks_first.h \
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
    $${PWD}/OAIListOfOrders.cpp \
    $${PWD}/OAIOrder.cpp \
    $${PWD}/OAIOrderHeader.cpp \
    $${PWD}/OAIOrderLineItem.cpp \
    $${PWD}/OAIOrderLineItem_quantities_inner.cpp \
    $${PWD}/OAIPaginationLinks.cpp \
    $${PWD}/OAIPaginationLinks_first.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp

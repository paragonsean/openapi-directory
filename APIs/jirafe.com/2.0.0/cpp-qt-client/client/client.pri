QT += network

HEADERS += \
# Models
    $${PWD}/OAIAttribute.h \
    $${PWD}/OAIBaseProduct.h \
    $${PWD}/OAIBatch.h \
    $${PWD}/OAICart.h \
    $${PWD}/OAICartItem.h \
    $${PWD}/OAICatalog.h \
    $${PWD}/OAICategory.h \
    $${PWD}/OAICustomer.h \
    $${PWD}/OAIOrder.h \
    $${PWD}/OAIOrderCancelled.h \
    $${PWD}/OAIOrderItem.h \
    $${PWD}/OAIParentCategory.h \
    $${PWD}/OAIProduct.h \
    $${PWD}/OAIUrl.h \
    $${PWD}/OAIVendor.h \
    $${PWD}/OAIVisit.h \
# APIs
    $${PWD}/OAIBatchApi.h \
    $${PWD}/OAICartApi.h \
    $${PWD}/OAICategoryApi.h \
    $${PWD}/OAICustomerApi.h \
    $${PWD}/OAIOrderApi.h \
    $${PWD}/OAIProductApi.h \
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
    $${PWD}/OAIAttribute.cpp \
    $${PWD}/OAIBaseProduct.cpp \
    $${PWD}/OAIBatch.cpp \
    $${PWD}/OAICart.cpp \
    $${PWD}/OAICartItem.cpp \
    $${PWD}/OAICatalog.cpp \
    $${PWD}/OAICategory.cpp \
    $${PWD}/OAICustomer.cpp \
    $${PWD}/OAIOrder.cpp \
    $${PWD}/OAIOrderCancelled.cpp \
    $${PWD}/OAIOrderItem.cpp \
    $${PWD}/OAIParentCategory.cpp \
    $${PWD}/OAIProduct.cpp \
    $${PWD}/OAIUrl.cpp \
    $${PWD}/OAIVendor.cpp \
    $${PWD}/OAIVisit.cpp \
# APIs
    $${PWD}/OAIBatchApi.cpp \
    $${PWD}/OAICartApi.cpp \
    $${PWD}/OAICategoryApi.cpp \
    $${PWD}/OAICustomerApi.cpp \
    $${PWD}/OAIOrderApi.cpp \
    $${PWD}/OAIProductApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp

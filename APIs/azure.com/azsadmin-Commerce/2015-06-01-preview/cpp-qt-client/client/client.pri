QT += network

HEADERS += \
# Models
    $${PWD}/OAIDisplay.h \
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIOperationList.h \
    $${PWD}/OAIResource.h \
    $${PWD}/OAIUsageAggregate.h \
    $${PWD}/OAIUsageAggregateModel.h \
    $${PWD}/OAIUsageAggregatePage.h \
# APIs
    $${PWD}/OAICommerceApi.h \
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
    $${PWD}/OAIDisplay.cpp \
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIOperationList.cpp \
    $${PWD}/OAIResource.cpp \
    $${PWD}/OAIUsageAggregate.cpp \
    $${PWD}/OAIUsageAggregateModel.cpp \
    $${PWD}/OAIUsageAggregatePage.cpp \
# APIs
    $${PWD}/OAICommerceApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp

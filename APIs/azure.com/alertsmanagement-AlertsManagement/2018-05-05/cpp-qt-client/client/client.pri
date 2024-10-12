QT += network

HEADERS += \
# Models
    $${PWD}/OAIAlert.h \
    $${PWD}/OAIAlertModification.h \
    $${PWD}/OAIAlertModificationItem.h \
    $${PWD}/OAIAlertModificationProperties.h \
    $${PWD}/OAIAlertProperties.h \
    $${PWD}/OAIAlertsList.h \
    $${PWD}/OAIAlertsSummary.h \
    $${PWD}/OAIAlertsSummaryGroup.h \
    $${PWD}/OAIAlertsSummaryGroupItem.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIErrorResponseBody.h \
    $${PWD}/OAIEssentials.h \
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIOperation_display.h \
    $${PWD}/OAIOperationsList.h \
    $${PWD}/OAIResource.h \
    $${PWD}/OAISmartGroup.h \
    $${PWD}/OAISmartGroupAggregatedProperty.h \
    $${PWD}/OAISmartGroupModification.h \
    $${PWD}/OAISmartGroupModificationItem.h \
    $${PWD}/OAISmartGroupModificationProperties.h \
    $${PWD}/OAISmartGroupProperties.h \
    $${PWD}/OAISmartGroupsList.h \
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
    $${PWD}/OAIAlert.cpp \
    $${PWD}/OAIAlertModification.cpp \
    $${PWD}/OAIAlertModificationItem.cpp \
    $${PWD}/OAIAlertModificationProperties.cpp \
    $${PWD}/OAIAlertProperties.cpp \
    $${PWD}/OAIAlertsList.cpp \
    $${PWD}/OAIAlertsSummary.cpp \
    $${PWD}/OAIAlertsSummaryGroup.cpp \
    $${PWD}/OAIAlertsSummaryGroupItem.cpp \
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAIErrorResponseBody.cpp \
    $${PWD}/OAIEssentials.cpp \
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIOperation_display.cpp \
    $${PWD}/OAIOperationsList.cpp \
    $${PWD}/OAIResource.cpp \
    $${PWD}/OAISmartGroup.cpp \
    $${PWD}/OAISmartGroupAggregatedProperty.cpp \
    $${PWD}/OAISmartGroupModification.cpp \
    $${PWD}/OAISmartGroupModificationItem.cpp \
    $${PWD}/OAISmartGroupModificationProperties.cpp \
    $${PWD}/OAISmartGroupProperties.cpp \
    $${PWD}/OAISmartGroupsList.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp

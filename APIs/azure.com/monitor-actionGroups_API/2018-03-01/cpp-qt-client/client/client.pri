QT += network

HEADERS += \
# Models
    $${PWD}/OAIActionGroup.h \
    $${PWD}/OAIActionGroupList.h \
    $${PWD}/OAIActionGroupPatch.h \
    $${PWD}/OAIActionGroupPatchBody.h \
    $${PWD}/OAIActionGroupResource.h \
    $${PWD}/OAIAutomationRunbookReceiver.h \
    $${PWD}/OAIAzureAppPushReceiver.h \
    $${PWD}/OAIAzureFunctionReceiver.h \
    $${PWD}/OAIEmailReceiver.h \
    $${PWD}/OAIEnableRequest.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIItsmReceiver.h \
    $${PWD}/OAILogicAppReceiver.h \
    $${PWD}/OAIReceiverStatus.h \
    $${PWD}/OAIResource.h \
    $${PWD}/OAISmsReceiver.h \
    $${PWD}/OAIVoiceReceiver.h \
    $${PWD}/OAIWebhookReceiver.h \
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
    $${PWD}/OAIActionGroup.cpp \
    $${PWD}/OAIActionGroupList.cpp \
    $${PWD}/OAIActionGroupPatch.cpp \
    $${PWD}/OAIActionGroupPatchBody.cpp \
    $${PWD}/OAIActionGroupResource.cpp \
    $${PWD}/OAIAutomationRunbookReceiver.cpp \
    $${PWD}/OAIAzureAppPushReceiver.cpp \
    $${PWD}/OAIAzureFunctionReceiver.cpp \
    $${PWD}/OAIEmailReceiver.cpp \
    $${PWD}/OAIEnableRequest.cpp \
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAIItsmReceiver.cpp \
    $${PWD}/OAILogicAppReceiver.cpp \
    $${PWD}/OAIReceiverStatus.cpp \
    $${PWD}/OAIResource.cpp \
    $${PWD}/OAISmsReceiver.cpp \
    $${PWD}/OAIVoiceReceiver.cpp \
    $${PWD}/OAIWebhookReceiver.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp

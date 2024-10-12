QT += network

HEADERS += \
# Models
    $${PWD}/OAIAgentDeviceId.h \
    $${PWD}/OAIAgentOtherDeviceId.h \
    $${PWD}/OAIDevice.h \
    $${PWD}/OAIDeviceInfo.h \
    $${PWD}/OAIDeviceNames.h \
    $${PWD}/OAIQueryRequest.h \
    $${PWD}/OAIQueryRequestInput.h \
    $${PWD}/OAIQueryRequestPayload.h \
    $${PWD}/OAIQueryResponse.h \
    $${PWD}/OAIQueryResponsePayload.h \
    $${PWD}/OAIReportStateAndNotificationDevice.h \
    $${PWD}/OAIReportStateAndNotificationRequest.h \
    $${PWD}/OAIReportStateAndNotificationResponse.h \
    $${PWD}/OAIRequestSyncDevicesRequest.h \
    $${PWD}/OAIStateAndNotificationPayload.h \
    $${PWD}/OAISyncRequest.h \
    $${PWD}/OAISyncResponse.h \
    $${PWD}/OAISyncResponsePayload.h \
# APIs
    $${PWD}/OAIAgentUsersApi.h \
    $${PWD}/OAIDevicesApi.h \
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
    $${PWD}/OAIAgentDeviceId.cpp \
    $${PWD}/OAIAgentOtherDeviceId.cpp \
    $${PWD}/OAIDevice.cpp \
    $${PWD}/OAIDeviceInfo.cpp \
    $${PWD}/OAIDeviceNames.cpp \
    $${PWD}/OAIQueryRequest.cpp \
    $${PWD}/OAIQueryRequestInput.cpp \
    $${PWD}/OAIQueryRequestPayload.cpp \
    $${PWD}/OAIQueryResponse.cpp \
    $${PWD}/OAIQueryResponsePayload.cpp \
    $${PWD}/OAIReportStateAndNotificationDevice.cpp \
    $${PWD}/OAIReportStateAndNotificationRequest.cpp \
    $${PWD}/OAIReportStateAndNotificationResponse.cpp \
    $${PWD}/OAIRequestSyncDevicesRequest.cpp \
    $${PWD}/OAIStateAndNotificationPayload.cpp \
    $${PWD}/OAISyncRequest.cpp \
    $${PWD}/OAISyncResponse.cpp \
    $${PWD}/OAISyncResponsePayload.cpp \
# APIs
    $${PWD}/OAIAgentUsersApi.cpp \
    $${PWD}/OAIDevicesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp

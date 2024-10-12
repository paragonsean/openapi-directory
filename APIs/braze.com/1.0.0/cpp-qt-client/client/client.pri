QT += network

HEADERS += \
# Models
    $${PWD}/OAIScheduleApiTriggeredCanvases_request.h \
    $${PWD}/OAIScheduleApiTriggeredCanvases_request_audience.h \
    $${PWD}/OAIScheduleApiTriggeredCanvases_request_audience_AND_inner.h \
    $${PWD}/OAIScheduleApiTriggeredCanvases_request_audience_AND_inner_custom_attribute.h \
    $${PWD}/OAIScheduleApiTriggeredCanvases_request_recipients_inner.h \
    $${PWD}/OAIScheduleApiTriggeredCanvases_request_schedule.h \
# APIs
    $${PWD}/OAICampaignApi.h \
    $${PWD}/OAICanvasApi.h \
    $${PWD}/OAIContentBlocksApi.h \
    $${PWD}/OAICustomEventsApi.h \
    $${PWD}/OAIEmailListsAddressesApi.h \
    $${PWD}/OAIEmailTemplatesApi.h \
    $${PWD}/OAIExportApi.h \
    $${PWD}/OAIKPIApi.h \
    $${PWD}/OAIMessagingApi.h \
    $${PWD}/OAINewsFeedApi.h \
    $${PWD}/OAISMSApi.h \
    $${PWD}/OAIScheduleMesagesApi.h \
    $${PWD}/OAISegmentApi.h \
    $${PWD}/OAISessionAnalyticsApi.h \
    $${PWD}/OAISubscriptionGroupsApi.h \
    $${PWD}/OAITemplatesApi.h \
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
    $${PWD}/OAIScheduleApiTriggeredCanvases_request.cpp \
    $${PWD}/OAIScheduleApiTriggeredCanvases_request_audience.cpp \
    $${PWD}/OAIScheduleApiTriggeredCanvases_request_audience_AND_inner.cpp \
    $${PWD}/OAIScheduleApiTriggeredCanvases_request_audience_AND_inner_custom_attribute.cpp \
    $${PWD}/OAIScheduleApiTriggeredCanvases_request_recipients_inner.cpp \
    $${PWD}/OAIScheduleApiTriggeredCanvases_request_schedule.cpp \
# APIs
    $${PWD}/OAICampaignApi.cpp \
    $${PWD}/OAICanvasApi.cpp \
    $${PWD}/OAIContentBlocksApi.cpp \
    $${PWD}/OAICustomEventsApi.cpp \
    $${PWD}/OAIEmailListsAddressesApi.cpp \
    $${PWD}/OAIEmailTemplatesApi.cpp \
    $${PWD}/OAIExportApi.cpp \
    $${PWD}/OAIKPIApi.cpp \
    $${PWD}/OAIMessagingApi.cpp \
    $${PWD}/OAINewsFeedApi.cpp \
    $${PWD}/OAISMSApi.cpp \
    $${PWD}/OAIScheduleMesagesApi.cpp \
    $${PWD}/OAISegmentApi.cpp \
    $${PWD}/OAISessionAnalyticsApi.cpp \
    $${PWD}/OAISubscriptionGroupsApi.cpp \
    $${PWD}/OAITemplatesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp

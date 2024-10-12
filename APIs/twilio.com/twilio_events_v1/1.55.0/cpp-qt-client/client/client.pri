QT += network

HEADERS += \
# Models
    $${PWD}/OAIEvents_v1_event_type.h \
    $${PWD}/OAIEvents_v1_schema.h \
    $${PWD}/OAIEvents_v1_schema_schema_version.h \
    $${PWD}/OAIEvents_v1_sink.h \
    $${PWD}/OAIEvents_v1_sink_sink_test.h \
    $${PWD}/OAIEvents_v1_sink_sink_validate.h \
    $${PWD}/OAIEvents_v1_subscription.h \
    $${PWD}/OAIEvents_v1_subscription_subscribed_event.h \
    $${PWD}/OAIListEventTypeResponse.h \
    $${PWD}/OAIListSchemaVersionResponse.h \
    $${PWD}/OAIListSchemaVersionResponse_meta.h \
    $${PWD}/OAIListSinkResponse.h \
    $${PWD}/OAIListSubscribedEventResponse.h \
    $${PWD}/OAIListSubscriptionResponse.h \
    $${PWD}/OAISink_enum_sink_type.h \
    $${PWD}/OAISink_enum_status.h \
# APIs
    $${PWD}/OAIEventsV1EventTypeApi.h \
    $${PWD}/OAIEventsV1SchemaApi.h \
    $${PWD}/OAIEventsV1SchemaVersionApi.h \
    $${PWD}/OAIEventsV1SinkApi.h \
    $${PWD}/OAIEventsV1SinkTestApi.h \
    $${PWD}/OAIEventsV1SinkValidateApi.h \
    $${PWD}/OAIEventsV1SubscribedEventApi.h \
    $${PWD}/OAIEventsV1SubscriptionApi.h \
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
    $${PWD}/OAIEvents_v1_event_type.cpp \
    $${PWD}/OAIEvents_v1_schema.cpp \
    $${PWD}/OAIEvents_v1_schema_schema_version.cpp \
    $${PWD}/OAIEvents_v1_sink.cpp \
    $${PWD}/OAIEvents_v1_sink_sink_test.cpp \
    $${PWD}/OAIEvents_v1_sink_sink_validate.cpp \
    $${PWD}/OAIEvents_v1_subscription.cpp \
    $${PWD}/OAIEvents_v1_subscription_subscribed_event.cpp \
    $${PWD}/OAIListEventTypeResponse.cpp \
    $${PWD}/OAIListSchemaVersionResponse.cpp \
    $${PWD}/OAIListSchemaVersionResponse_meta.cpp \
    $${PWD}/OAIListSinkResponse.cpp \
    $${PWD}/OAIListSubscribedEventResponse.cpp \
    $${PWD}/OAIListSubscriptionResponse.cpp \
    $${PWD}/OAISink_enum_sink_type.cpp \
    $${PWD}/OAISink_enum_status.cpp \
# APIs
    $${PWD}/OAIEventsV1EventTypeApi.cpp \
    $${PWD}/OAIEventsV1SchemaApi.cpp \
    $${PWD}/OAIEventsV1SchemaVersionApi.cpp \
    $${PWD}/OAIEventsV1SinkApi.cpp \
    $${PWD}/OAIEventsV1SinkTestApi.cpp \
    $${PWD}/OAIEventsV1SinkValidateApi.cpp \
    $${PWD}/OAIEventsV1SubscribedEventApi.cpp \
    $${PWD}/OAIEventsV1SubscriptionApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp

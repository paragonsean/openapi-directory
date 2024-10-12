QT += network

HEADERS += \
# Models
    $${PWD}/OAIAccount_usage_record_enum_granularity.h \
    $${PWD}/OAICommand_enum_command_mode.h \
    $${PWD}/OAICommand_enum_direction.h \
    $${PWD}/OAICommand_enum_status.h \
    $${PWD}/OAICommand_enum_transport.h \
    $${PWD}/OAIListAccountUsageRecordResponse.h \
    $${PWD}/OAIListCommandResponse.h \
    $${PWD}/OAIListCommandResponse_meta.h \
    $${PWD}/OAIListDataSessionResponse.h \
    $${PWD}/OAIListRatePlanResponse.h \
    $${PWD}/OAIListSimResponse.h \
    $${PWD}/OAIListUsageRecordResponse.h \
    $${PWD}/OAIRate_plan_enum_data_limit_strategy.h \
    $${PWD}/OAISim_enum_reset_status.h \
    $${PWD}/OAISim_enum_status.h \
    $${PWD}/OAIUsage_record_enum_granularity.h \
    $${PWD}/OAIWireless_v1_account_usage_record.h \
    $${PWD}/OAIWireless_v1_command.h \
    $${PWD}/OAIWireless_v1_rate_plan.h \
    $${PWD}/OAIWireless_v1_sim.h \
    $${PWD}/OAIWireless_v1_sim_data_session.h \
    $${PWD}/OAIWireless_v1_sim_usage_record.h \
# APIs
    $${PWD}/OAIWirelessV1CommandApi.h \
    $${PWD}/OAIWirelessV1DataSessionApi.h \
    $${PWD}/OAIWirelessV1RatePlanApi.h \
    $${PWD}/OAIWirelessV1SimApi.h \
    $${PWD}/OAIWirelessV1UsageRecordApi.h \
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
    $${PWD}/OAIAccount_usage_record_enum_granularity.cpp \
    $${PWD}/OAICommand_enum_command_mode.cpp \
    $${PWD}/OAICommand_enum_direction.cpp \
    $${PWD}/OAICommand_enum_status.cpp \
    $${PWD}/OAICommand_enum_transport.cpp \
    $${PWD}/OAIListAccountUsageRecordResponse.cpp \
    $${PWD}/OAIListCommandResponse.cpp \
    $${PWD}/OAIListCommandResponse_meta.cpp \
    $${PWD}/OAIListDataSessionResponse.cpp \
    $${PWD}/OAIListRatePlanResponse.cpp \
    $${PWD}/OAIListSimResponse.cpp \
    $${PWD}/OAIListUsageRecordResponse.cpp \
    $${PWD}/OAIRate_plan_enum_data_limit_strategy.cpp \
    $${PWD}/OAISim_enum_reset_status.cpp \
    $${PWD}/OAISim_enum_status.cpp \
    $${PWD}/OAIUsage_record_enum_granularity.cpp \
    $${PWD}/OAIWireless_v1_account_usage_record.cpp \
    $${PWD}/OAIWireless_v1_command.cpp \
    $${PWD}/OAIWireless_v1_rate_plan.cpp \
    $${PWD}/OAIWireless_v1_sim.cpp \
    $${PWD}/OAIWireless_v1_sim_data_session.cpp \
    $${PWD}/OAIWireless_v1_sim_usage_record.cpp \
# APIs
    $${PWD}/OAIWirelessV1CommandApi.cpp \
    $${PWD}/OAIWirelessV1DataSessionApi.cpp \
    $${PWD}/OAIWirelessV1RatePlanApi.cpp \
    $${PWD}/OAIWirelessV1SimApi.cpp \
    $${PWD}/OAIWirelessV1UsageRecordApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp

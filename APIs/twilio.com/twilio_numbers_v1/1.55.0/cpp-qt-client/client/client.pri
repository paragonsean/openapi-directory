QT += network

HEADERS += \
# Models
    $${PWD}/OAIBulk_eligibility_enum_eligibility_status.h \
    $${PWD}/OAIBulk_eligibility_enum_eligibility_sub_status.h \
    $${PWD}/OAIEligibility_enum_eligibility_status.h \
    $${PWD}/OAIEligibility_enum_eligibility_sub_status.h \
    $${PWD}/OAINumbers_v1_bulk_eligibility.h \
    $${PWD}/OAINumbers_v1_eligibility.h \
    $${PWD}/OAINumbers_v1_porting_bulk_portability.h \
    $${PWD}/OAINumbers_v1_porting_port_in.h \
    $${PWD}/OAINumbers_v1_porting_port_in_fetch.h \
    $${PWD}/OAINumbers_v1_porting_portability.h \
    $${PWD}/OAIPorting_bulk_portability_enum_status.h \
    $${PWD}/OAIPorting_portability_enum_number_type.h \
# APIs
    $${PWD}/OAINumbersV1BulkEligibilityApi.h \
    $${PWD}/OAINumbersV1PortingBulkPortabilityApi.h \
    $${PWD}/OAINumbersV1PortingPortInFetchApi.h \
    $${PWD}/OAINumbersV1PortingPortabilityApi.h \
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
    $${PWD}/OAIBulk_eligibility_enum_eligibility_status.cpp \
    $${PWD}/OAIBulk_eligibility_enum_eligibility_sub_status.cpp \
    $${PWD}/OAIEligibility_enum_eligibility_status.cpp \
    $${PWD}/OAIEligibility_enum_eligibility_sub_status.cpp \
    $${PWD}/OAINumbers_v1_bulk_eligibility.cpp \
    $${PWD}/OAINumbers_v1_eligibility.cpp \
    $${PWD}/OAINumbers_v1_porting_bulk_portability.cpp \
    $${PWD}/OAINumbers_v1_porting_port_in.cpp \
    $${PWD}/OAINumbers_v1_porting_port_in_fetch.cpp \
    $${PWD}/OAINumbers_v1_porting_portability.cpp \
    $${PWD}/OAIPorting_bulk_portability_enum_status.cpp \
    $${PWD}/OAIPorting_portability_enum_number_type.cpp \
# APIs
    $${PWD}/OAINumbersV1BulkEligibilityApi.cpp \
    $${PWD}/OAINumbersV1PortingBulkPortabilityApi.cpp \
    $${PWD}/OAINumbersV1PortingPortInFetchApi.cpp \
    $${PWD}/OAINumbersV1PortingPortabilityApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp

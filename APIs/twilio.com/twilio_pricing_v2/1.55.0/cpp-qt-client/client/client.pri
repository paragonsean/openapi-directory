QT += network

HEADERS += \
# Models
    $${PWD}/OAIListTrunkingCountryResponse.h \
    $${PWD}/OAIListTrunkingCountryResponse_meta.h \
    $${PWD}/OAIListVoiceCountryResponse.h \
    $${PWD}/OAIPricing_v2_trunking_country.h \
    $${PWD}/OAIPricing_v2_trunking_country_instance.h \
    $${PWD}/OAIPricing_v2_trunking_country_instance_originating_call_prices_inner.h \
    $${PWD}/OAIPricing_v2_trunking_country_instance_terminating_prefix_prices_inner.h \
    $${PWD}/OAIPricing_v2_trunking_number.h \
    $${PWD}/OAIPricing_v2_trunking_number_originating_call_price.h \
    $${PWD}/OAIPricing_v2_voice.h \
    $${PWD}/OAIPricing_v2_voice_voice_country.h \
    $${PWD}/OAIPricing_v2_voice_voice_country_instance.h \
    $${PWD}/OAIPricing_v2_voice_voice_number.h \
    $${PWD}/OAIPricing_v2_voice_voice_number_inbound_call_price.h \
    $${PWD}/OAIPricing_v2_voice_voice_number_outbound_call_prices_inner.h \
# APIs
    $${PWD}/OAIPricingV2CountryApi.h \
    $${PWD}/OAIPricingV2NumberApi.h \
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
    $${PWD}/OAIListTrunkingCountryResponse.cpp \
    $${PWD}/OAIListTrunkingCountryResponse_meta.cpp \
    $${PWD}/OAIListVoiceCountryResponse.cpp \
    $${PWD}/OAIPricing_v2_trunking_country.cpp \
    $${PWD}/OAIPricing_v2_trunking_country_instance.cpp \
    $${PWD}/OAIPricing_v2_trunking_country_instance_originating_call_prices_inner.cpp \
    $${PWD}/OAIPricing_v2_trunking_country_instance_terminating_prefix_prices_inner.cpp \
    $${PWD}/OAIPricing_v2_trunking_number.cpp \
    $${PWD}/OAIPricing_v2_trunking_number_originating_call_price.cpp \
    $${PWD}/OAIPricing_v2_voice.cpp \
    $${PWD}/OAIPricing_v2_voice_voice_country.cpp \
    $${PWD}/OAIPricing_v2_voice_voice_country_instance.cpp \
    $${PWD}/OAIPricing_v2_voice_voice_number.cpp \
    $${PWD}/OAIPricing_v2_voice_voice_number_inbound_call_price.cpp \
    $${PWD}/OAIPricing_v2_voice_voice_number_outbound_call_prices_inner.cpp \
# APIs
    $${PWD}/OAIPricingV2CountryApi.cpp \
    $${PWD}/OAIPricingV2NumberApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp

QT += network

HEADERS += \
# Models
    $${PWD}/OAIListMessagingCountryResponse.h \
    $${PWD}/OAIListMessagingCountryResponse_meta.h \
    $${PWD}/OAIListPhoneNumberCountryResponse.h \
    $${PWD}/OAIListVoiceCountryResponse.h \
    $${PWD}/OAIPricing_v1_messaging.h \
    $${PWD}/OAIPricing_v1_messaging_messaging_country.h \
    $${PWD}/OAIPricing_v1_messaging_messaging_country_instance.h \
    $${PWD}/OAIPricing_v1_messaging_messaging_country_instance_inbound_sms_prices_inner.h \
    $${PWD}/OAIPricing_v1_messaging_messaging_country_instance_outbound_sms_prices_inner.h \
    $${PWD}/OAIPricing_v1_messaging_messaging_country_instance_outbound_sms_prices_inner_prices_inner.h \
    $${PWD}/OAIPricing_v1_phone_number.h \
    $${PWD}/OAIPricing_v1_phone_number_phone_number_country.h \
    $${PWD}/OAIPricing_v1_phone_number_phone_number_country_instance.h \
    $${PWD}/OAIPricing_v1_phone_number_phone_number_country_instance_phone_number_prices_inner.h \
    $${PWD}/OAIPricing_v1_voice.h \
    $${PWD}/OAIPricing_v1_voice_voice_country.h \
    $${PWD}/OAIPricing_v1_voice_voice_country_instance.h \
    $${PWD}/OAIPricing_v1_voice_voice_country_instance_inbound_call_prices_inner.h \
    $${PWD}/OAIPricing_v1_voice_voice_country_instance_outbound_prefix_prices_inner.h \
    $${PWD}/OAIPricing_v1_voice_voice_number.h \
    $${PWD}/OAIPricing_v1_voice_voice_number_inbound_call_price.h \
    $${PWD}/OAIPricing_v1_voice_voice_number_outbound_call_price.h \
# APIs
    $${PWD}/OAIPricingV1CountryApi.h \
    $${PWD}/OAIPricingV1NumberApi.h \
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
    $${PWD}/OAIListMessagingCountryResponse.cpp \
    $${PWD}/OAIListMessagingCountryResponse_meta.cpp \
    $${PWD}/OAIListPhoneNumberCountryResponse.cpp \
    $${PWD}/OAIListVoiceCountryResponse.cpp \
    $${PWD}/OAIPricing_v1_messaging.cpp \
    $${PWD}/OAIPricing_v1_messaging_messaging_country.cpp \
    $${PWD}/OAIPricing_v1_messaging_messaging_country_instance.cpp \
    $${PWD}/OAIPricing_v1_messaging_messaging_country_instance_inbound_sms_prices_inner.cpp \
    $${PWD}/OAIPricing_v1_messaging_messaging_country_instance_outbound_sms_prices_inner.cpp \
    $${PWD}/OAIPricing_v1_messaging_messaging_country_instance_outbound_sms_prices_inner_prices_inner.cpp \
    $${PWD}/OAIPricing_v1_phone_number.cpp \
    $${PWD}/OAIPricing_v1_phone_number_phone_number_country.cpp \
    $${PWD}/OAIPricing_v1_phone_number_phone_number_country_instance.cpp \
    $${PWD}/OAIPricing_v1_phone_number_phone_number_country_instance_phone_number_prices_inner.cpp \
    $${PWD}/OAIPricing_v1_voice.cpp \
    $${PWD}/OAIPricing_v1_voice_voice_country.cpp \
    $${PWD}/OAIPricing_v1_voice_voice_country_instance.cpp \
    $${PWD}/OAIPricing_v1_voice_voice_country_instance_inbound_call_prices_inner.cpp \
    $${PWD}/OAIPricing_v1_voice_voice_country_instance_outbound_prefix_prices_inner.cpp \
    $${PWD}/OAIPricing_v1_voice_voice_number.cpp \
    $${PWD}/OAIPricing_v1_voice_voice_number_inbound_call_price.cpp \
    $${PWD}/OAIPricing_v1_voice_voice_number_outbound_call_price.cpp \
# APIs
    $${PWD}/OAIPricingV1CountryApi.cpp \
    $${PWD}/OAIPricingV1NumberApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp

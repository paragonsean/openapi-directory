QT += network

HEADERS += \
# Models
    $${PWD}/OAIEmailValidation_200_response.h \
    $${PWD}/OAIEmailValidation_200_response_associated_names.h \
    $${PWD}/OAIEmailValidation_200_response_associated_phone_numbers.h \
    $${PWD}/OAIEmailValidation_200_response_domain_age.h \
    $${PWD}/OAIEmailValidation_400_response.h \
    $${PWD}/OAIMaliciousUrlScanner_200_response.h \
    $${PWD}/OAIMaliciousUrlScanner_200_response_domain_age.h \
    $${PWD}/OAIPhoneValidation_200_response.h \
    $${PWD}/OAIPhoneValidation_200_response_associated_email_addresses.h \
# APIs
    $${PWD}/OAIEmailValidationApi.h \
    $${PWD}/OAIMaliciousUrlScannerApi.h \
    $${PWD}/OAIPhoneValidationApi.h \
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
    $${PWD}/OAIEmailValidation_200_response.cpp \
    $${PWD}/OAIEmailValidation_200_response_associated_names.cpp \
    $${PWD}/OAIEmailValidation_200_response_associated_phone_numbers.cpp \
    $${PWD}/OAIEmailValidation_200_response_domain_age.cpp \
    $${PWD}/OAIEmailValidation_400_response.cpp \
    $${PWD}/OAIMaliciousUrlScanner_200_response.cpp \
    $${PWD}/OAIMaliciousUrlScanner_200_response_domain_age.cpp \
    $${PWD}/OAIPhoneValidation_200_response.cpp \
    $${PWD}/OAIPhoneValidation_200_response_associated_email_addresses.cpp \
# APIs
    $${PWD}/OAIEmailValidationApi.cpp \
    $${PWD}/OAIMaliciousUrlScannerApi.cpp \
    $${PWD}/OAIPhoneValidationApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp

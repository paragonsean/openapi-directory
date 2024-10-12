QT += network

HEADERS += \
# Models
    $${PWD}/OAILookups_v2_phone_number.h \
    $${PWD}/OAIPhone_number_enum_type.h \
    $${PWD}/OAIPhone_number_enum_validation_error.h \
# APIs
    $${PWD}/OAILookupsV2PhoneNumberApi.h \
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
    $${PWD}/OAILookups_v2_phone_number.cpp \
    $${PWD}/OAIPhone_number_enum_type.cpp \
    $${PWD}/OAIPhone_number_enum_validation_error.cpp \
# APIs
    $${PWD}/OAILookupsV2PhoneNumberApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp

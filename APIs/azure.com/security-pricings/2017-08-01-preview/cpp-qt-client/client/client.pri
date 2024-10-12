QT += network

HEADERS += \
# Models
    $${PWD}/OAIPricing.h \
    $${PWD}/OAIPricingList.h \
    $${PWD}/OAIPricingProperties.h \
    $${PWD}/OAIPricings_List_default_response.h \
    $${PWD}/OAIPricings_List_default_response_error.h \
# APIs
    $${PWD}/OAIPricingsApi.h \
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
    $${PWD}/OAIPricing.cpp \
    $${PWD}/OAIPricingList.cpp \
    $${PWD}/OAIPricingProperties.cpp \
    $${PWD}/OAIPricings_List_default_response.cpp \
    $${PWD}/OAIPricings_List_default_response_error.cpp \
# APIs
    $${PWD}/OAIPricingsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp

QT += network

HEADERS += \
# Models
    $${PWD}/OAI_address_autocomplete_post_request.h \
    $${PWD}/OAI_contact_enrich_post_request.h \
    $${PWD}/OAI_contact_enrich_post_request_Address.h \
    $${PWD}/OAI_email_enrich_post_request.h \
    $${PWD}/OAI_phone_enrich_post_request.h \
# APIs
    $${PWD}/OAIDefaultApi.h \
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
    $${PWD}/OAI_address_autocomplete_post_request.cpp \
    $${PWD}/OAI_contact_enrich_post_request.cpp \
    $${PWD}/OAI_contact_enrich_post_request_Address.cpp \
    $${PWD}/OAI_email_enrich_post_request.cpp \
    $${PWD}/OAI_phone_enrich_post_request.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp

QT += network

HEADERS += \
# Models
    $${PWD}/OAIContact.h \
    $${PWD}/OAIContactAdd.h \
    $${PWD}/OAIContactCustomFieldSchema.h \
    $${PWD}/OAIContactList.h \
    $${PWD}/OAIContactListEventCustomization.h \
    $${PWD}/OAIContactListPage.h \
    $${PWD}/OAIContactListUpdate.h \
    $${PWD}/OAIContactPage.h \
    $${PWD}/OAIContactUpdate.h \
    $${PWD}/OAINewId.h \
    $${PWD}/OAISubscriptionRequest.h \
    $${PWD}/OAI_contacts_get_401_response_inner.h \
    $${PWD}/OAI_contacts_get_404_response_inner.h \
    $${PWD}/OAI_contacts_get_422_response_inner.h \
# APIs
    $${PWD}/OAIContactsApi.h \
    $${PWD}/OAIListsApi.h \
    $${PWD}/OAISubscriptionApi.h \
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
    $${PWD}/OAIContact.cpp \
    $${PWD}/OAIContactAdd.cpp \
    $${PWD}/OAIContactCustomFieldSchema.cpp \
    $${PWD}/OAIContactList.cpp \
    $${PWD}/OAIContactListEventCustomization.cpp \
    $${PWD}/OAIContactListPage.cpp \
    $${PWD}/OAIContactListUpdate.cpp \
    $${PWD}/OAIContactPage.cpp \
    $${PWD}/OAIContactUpdate.cpp \
    $${PWD}/OAINewId.cpp \
    $${PWD}/OAISubscriptionRequest.cpp \
    $${PWD}/OAI_contacts_get_401_response_inner.cpp \
    $${PWD}/OAI_contacts_get_404_response_inner.cpp \
    $${PWD}/OAI_contacts_get_422_response_inner.cpp \
# APIs
    $${PWD}/OAIContactsApi.cpp \
    $${PWD}/OAIListsApi.cpp \
    $${PWD}/OAISubscriptionApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp

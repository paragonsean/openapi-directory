QT += network

HEADERS += \
# Models
    $${PWD}/OAIAccount.h \
    $${PWD}/OAIAdmin.h \
    $${PWD}/OAIInvitation.h \
    $${PWD}/OAIListAccountAdminsResponse.h \
    $${PWD}/OAIListAccountsResponse.h \
    $${PWD}/OAIListInvitationsResponse.h \
    $${PWD}/OAIListLocationAdminsResponse.h \
    $${PWD}/OAIOrganizationInfo.h \
    $${PWD}/OAIPostalAddress.h \
    $${PWD}/OAITargetLocation.h \
    $${PWD}/OAITransferLocationRequest.h \
# APIs
    $${PWD}/OAIAccountsApi.h \
    $${PWD}/OAILocationsApi.h \
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
    $${PWD}/OAIAccount.cpp \
    $${PWD}/OAIAdmin.cpp \
    $${PWD}/OAIInvitation.cpp \
    $${PWD}/OAIListAccountAdminsResponse.cpp \
    $${PWD}/OAIListAccountsResponse.cpp \
    $${PWD}/OAIListInvitationsResponse.cpp \
    $${PWD}/OAIListLocationAdminsResponse.cpp \
    $${PWD}/OAIOrganizationInfo.cpp \
    $${PWD}/OAIPostalAddress.cpp \
    $${PWD}/OAITargetLocation.cpp \
    $${PWD}/OAITransferLocationRequest.cpp \
# APIs
    $${PWD}/OAIAccountsApi.cpp \
    $${PWD}/OAILocationsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp

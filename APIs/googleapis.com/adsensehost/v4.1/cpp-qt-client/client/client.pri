QT += network

HEADERS += \
# Models
    $${PWD}/OAIAccount.h \
    $${PWD}/OAIAccounts.h \
    $${PWD}/OAIAdClient.h \
    $${PWD}/OAIAdClients.h \
    $${PWD}/OAIAdCode.h \
    $${PWD}/OAIAdStyle.h \
    $${PWD}/OAIAdStyle_colors.h \
    $${PWD}/OAIAdStyle_font.h \
    $${PWD}/OAIAdUnit.h \
    $${PWD}/OAIAdUnit_contentAdsSettings.h \
    $${PWD}/OAIAdUnit_contentAdsSettings_backupOption.h \
    $${PWD}/OAIAdUnit_mobileContentAdsSettings.h \
    $${PWD}/OAIAdUnits.h \
    $${PWD}/OAIAssociationSession.h \
    $${PWD}/OAICustomChannel.h \
    $${PWD}/OAICustomChannels.h \
    $${PWD}/OAIReport.h \
    $${PWD}/OAIReport_headers_inner.h \
    $${PWD}/OAIUrlChannel.h \
    $${PWD}/OAIUrlChannels.h \
# APIs
    $${PWD}/OAIAccountsApi.h \
    $${PWD}/OAIAdclientsApi.h \
    $${PWD}/OAIAssociationsessionsApi.h \
    $${PWD}/OAICustomchannelsApi.h \
    $${PWD}/OAIReportsApi.h \
    $${PWD}/OAIUrlchannelsApi.h \
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
    $${PWD}/OAIAccounts.cpp \
    $${PWD}/OAIAdClient.cpp \
    $${PWD}/OAIAdClients.cpp \
    $${PWD}/OAIAdCode.cpp \
    $${PWD}/OAIAdStyle.cpp \
    $${PWD}/OAIAdStyle_colors.cpp \
    $${PWD}/OAIAdStyle_font.cpp \
    $${PWD}/OAIAdUnit.cpp \
    $${PWD}/OAIAdUnit_contentAdsSettings.cpp \
    $${PWD}/OAIAdUnit_contentAdsSettings_backupOption.cpp \
    $${PWD}/OAIAdUnit_mobileContentAdsSettings.cpp \
    $${PWD}/OAIAdUnits.cpp \
    $${PWD}/OAIAssociationSession.cpp \
    $${PWD}/OAICustomChannel.cpp \
    $${PWD}/OAICustomChannels.cpp \
    $${PWD}/OAIReport.cpp \
    $${PWD}/OAIReport_headers_inner.cpp \
    $${PWD}/OAIUrlChannel.cpp \
    $${PWD}/OAIUrlChannels.cpp \
# APIs
    $${PWD}/OAIAccountsApi.cpp \
    $${PWD}/OAIAdclientsApi.cpp \
    $${PWD}/OAIAssociationsessionsApi.cpp \
    $${PWD}/OAICustomchannelsApi.cpp \
    $${PWD}/OAIReportsApi.cpp \
    $${PWD}/OAIUrlchannelsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp

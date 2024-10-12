QT += network

HEADERS += \
# Models
    $${PWD}/OAIAcquisition.h \
    $${PWD}/OAIAddress.h \
    $${PWD}/OAIBasic_results.h \
    $${PWD}/OAICeo.h \
    $${PWD}/OAICompany.h \
    $${PWD}/OAICompanyBasicSearchVO.h \
    $${PWD}/OAICompanyBasicVO.h \
    $${PWD}/OAICompanyCompetitorVO.h \
    $${PWD}/OAICompanySearchResultVO.h \
    $${PWD}/OAICompetitorBasicVO.h \
    $${PWD}/OAICompetitors.h \
    $${PWD}/OAIFeedsVO.h \
    $${PWD}/OAIFunding.h \
    $${PWD}/OAIInvestor.h \
    $${PWD}/OAIResults.h \
    $${PWD}/OAISectorVO.h \
    $${PWD}/OAIStock.h \
# APIs
    $${PWD}/OAICompanyAPIApi.h \
    $${PWD}/OAICompanyPremiumAPIApi.h \
    $${PWD}/OAICompetitorAPIApi.h \
    $${PWD}/OAICompetitorPremiumAPIApi.h \
    $${PWD}/OAIFeedAPIApi.h \
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
    $${PWD}/OAIAcquisition.cpp \
    $${PWD}/OAIAddress.cpp \
    $${PWD}/OAIBasic_results.cpp \
    $${PWD}/OAICeo.cpp \
    $${PWD}/OAICompany.cpp \
    $${PWD}/OAICompanyBasicSearchVO.cpp \
    $${PWD}/OAICompanyBasicVO.cpp \
    $${PWD}/OAICompanyCompetitorVO.cpp \
    $${PWD}/OAICompanySearchResultVO.cpp \
    $${PWD}/OAICompetitorBasicVO.cpp \
    $${PWD}/OAICompetitors.cpp \
    $${PWD}/OAIFeedsVO.cpp \
    $${PWD}/OAIFunding.cpp \
    $${PWD}/OAIInvestor.cpp \
    $${PWD}/OAIResults.cpp \
    $${PWD}/OAISectorVO.cpp \
    $${PWD}/OAIStock.cpp \
# APIs
    $${PWD}/OAICompanyAPIApi.cpp \
    $${PWD}/OAICompanyPremiumAPIApi.cpp \
    $${PWD}/OAICompetitorAPIApi.cpp \
    $${PWD}/OAICompetitorPremiumAPIApi.cpp \
    $${PWD}/OAIFeedAPIApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp

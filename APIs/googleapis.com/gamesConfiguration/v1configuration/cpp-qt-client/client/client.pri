QT += network

HEADERS += \
# Models
    $${PWD}/OAIAchievementConfiguration.h \
    $${PWD}/OAIAchievementConfigurationDetail.h \
    $${PWD}/OAIAchievementConfigurationListResponse.h \
    $${PWD}/OAIGamesNumberAffixConfiguration.h \
    $${PWD}/OAIGamesNumberFormatConfiguration.h \
    $${PWD}/OAILeaderboardConfiguration.h \
    $${PWD}/OAILeaderboardConfigurationDetail.h \
    $${PWD}/OAILeaderboardConfigurationListResponse.h \
    $${PWD}/OAILocalizedString.h \
    $${PWD}/OAILocalizedStringBundle.h \
# APIs
    $${PWD}/OAIAchievementConfigurationsApi.h \
    $${PWD}/OAILeaderboardConfigurationsApi.h \
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
    $${PWD}/OAIAchievementConfiguration.cpp \
    $${PWD}/OAIAchievementConfigurationDetail.cpp \
    $${PWD}/OAIAchievementConfigurationListResponse.cpp \
    $${PWD}/OAIGamesNumberAffixConfiguration.cpp \
    $${PWD}/OAIGamesNumberFormatConfiguration.cpp \
    $${PWD}/OAILeaderboardConfiguration.cpp \
    $${PWD}/OAILeaderboardConfigurationDetail.cpp \
    $${PWD}/OAILeaderboardConfigurationListResponse.cpp \
    $${PWD}/OAILocalizedString.cpp \
    $${PWD}/OAILocalizedStringBundle.cpp \
# APIs
    $${PWD}/OAIAchievementConfigurationsApi.cpp \
    $${PWD}/OAILeaderboardConfigurationsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp

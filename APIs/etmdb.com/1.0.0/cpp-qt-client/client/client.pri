QT += network

HEADERS += \
# Models
# APIs
    $${PWD}/OAICinemaApi.h \
    $${PWD}/OAICinemaDetailApi.h \
    $${PWD}/OAICinemaScheduleApi.h \
    $${PWD}/OAICinemaSheduleShowtimeApi.h \
    $${PWD}/OAICompanyApi.h \
    $${PWD}/OAICompanyCreditsApi.h \
    $${PWD}/OAIFilmographyApi.h \
    $${PWD}/OAIFilmographyTypeApi.h \
    $${PWD}/OAIGenreApi.h \
    $${PWD}/OAIGenreTypeApi.h \
    $${PWD}/OAIJobApi.h \
    $${PWD}/OAIMediaApi.h \
    $${PWD}/OAIMovieApi.h \
    $${PWD}/OAIMovieCastApi.h \
    $${PWD}/OAINewsApi.h \
    $${PWD}/OAIPeopleApi.h \
    $${PWD}/OAIShowtimeApi.h \
    $${PWD}/OAIWatchlistApi.h \
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
# APIs
    $${PWD}/OAICinemaApi.cpp \
    $${PWD}/OAICinemaDetailApi.cpp \
    $${PWD}/OAICinemaScheduleApi.cpp \
    $${PWD}/OAICinemaSheduleShowtimeApi.cpp \
    $${PWD}/OAICompanyApi.cpp \
    $${PWD}/OAICompanyCreditsApi.cpp \
    $${PWD}/OAIFilmographyApi.cpp \
    $${PWD}/OAIFilmographyTypeApi.cpp \
    $${PWD}/OAIGenreApi.cpp \
    $${PWD}/OAIGenreTypeApi.cpp \
    $${PWD}/OAIJobApi.cpp \
    $${PWD}/OAIMediaApi.cpp \
    $${PWD}/OAIMovieApi.cpp \
    $${PWD}/OAIMovieCastApi.cpp \
    $${PWD}/OAINewsApi.cpp \
    $${PWD}/OAIPeopleApi.cpp \
    $${PWD}/OAIShowtimeApi.cpp \
    $${PWD}/OAIWatchlistApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp

/**
 * Golf v2
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIPlayerRound.h
 *
 * 
 */

#ifndef OAIPlayerRound_H
#define OAIPlayerRound_H

#include <QJsonObject>

#include "OAIPlayerHole.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIPlayerHole;

class OAIPlayerRound : public OAIObject {
public:
    OAIPlayerRound();
    OAIPlayerRound(QString json);
    ~OAIPlayerRound() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isBackNineStart() const;
    void setBackNineStart(const bool &back_nine_start);
    bool is_back_nine_start_Set() const;
    bool is_back_nine_start_Valid() const;

    qint32 getBirdies() const;
    void setBirdies(const qint32 &birdies);
    bool is_birdies_Set() const;
    bool is_birdies_Valid() const;

    bool isBogeyFree() const;
    void setBogeyFree(const bool &bogey_free);
    bool is_bogey_free_Set() const;
    bool is_bogey_free_Valid() const;

    qint32 getBogeys() const;
    void setBogeys(const qint32 &bogeys);
    bool is_bogeys_Set() const;
    bool is_bogeys_Valid() const;

    double getBounceBackCount() const;
    void setBounceBackCount(const double &bounce_back_count);
    bool is_bounce_back_count_Set() const;
    bool is_bounce_back_count_Valid() const;

    double getConsecutiveBirdieOrBetterCount() const;
    void setConsecutiveBirdieOrBetterCount(const double &consecutive_birdie_or_better_count);
    bool is_consecutive_birdie_or_better_count_Set() const;
    bool is_consecutive_birdie_or_better_count_Valid() const;

    QString getDay() const;
    void setDay(const QString &day);
    bool is_day_Set() const;
    bool is_day_Valid() const;

    qint32 getDoubleBogeys() const;
    void setDoubleBogeys(const qint32 &double_bogeys);
    bool is_double_bogeys_Set() const;
    bool is_double_bogeys_Valid() const;

    qint32 getDoubleEagles() const;
    void setDoubleEagles(const qint32 &double_eagles);
    bool is_double_eagles_Set() const;
    bool is_double_eagles_Valid() const;

    qint32 getEagles() const;
    void setEagles(const qint32 &eagles);
    bool is_eagles_Set() const;
    bool is_eagles_Valid() const;

    qint32 getHoleInOnes() const;
    void setHoleInOnes(const qint32 &hole_in_ones);
    bool is_hole_in_ones_Set() const;
    bool is_hole_in_ones_Valid() const;

    QList<OAIPlayerHole> getHoles() const;
    void setHoles(const QList<OAIPlayerHole> &holes);
    bool is_holes_Set() const;
    bool is_holes_Valid() const;

    bool isIncludesFiveOrMoreBirdiesOrBetter() const;
    void setIncludesFiveOrMoreBirdiesOrBetter(const bool &includes_five_or_more_birdies_or_better);
    bool is_includes_five_or_more_birdies_or_better_Set() const;
    bool is_includes_five_or_more_birdies_or_better_Valid() const;

    bool isIncludesStreakOfFiveBirdiesOrBetter() const;
    void setIncludesStreakOfFiveBirdiesOrBetter(const bool &includes_streak_of_five_birdies_or_better);
    bool is_includes_streak_of_five_birdies_or_better_Set() const;
    bool is_includes_streak_of_five_birdies_or_better_Valid() const;

    bool isIncludesStreakOfFourBirdiesOrBetter() const;
    void setIncludesStreakOfFourBirdiesOrBetter(const bool &includes_streak_of_four_birdies_or_better);
    bool is_includes_streak_of_four_birdies_or_better_Set() const;
    bool is_includes_streak_of_four_birdies_or_better_Valid() const;

    bool isIncludesStreakOfSixBirdiesOrBetter() const;
    void setIncludesStreakOfSixBirdiesOrBetter(const bool &includes_streak_of_six_birdies_or_better);
    bool is_includes_streak_of_six_birdies_or_better_Set() const;
    bool is_includes_streak_of_six_birdies_or_better_Valid() const;

    bool isIncludesStreakOfThreeBirdiesOrBetter() const;
    void setIncludesStreakOfThreeBirdiesOrBetter(const bool &includes_streak_of_three_birdies_or_better);
    bool is_includes_streak_of_three_birdies_or_better_Set() const;
    bool is_includes_streak_of_three_birdies_or_better_Valid() const;

    double getLongestBirdieOrBetterStreak() const;
    void setLongestBirdieOrBetterStreak(const double &longest_birdie_or_better_streak);
    bool is_longest_birdie_or_better_streak_Set() const;
    bool is_longest_birdie_or_better_streak_Valid() const;

    qint32 getNumber() const;
    void setNumber(const qint32 &number);
    bool is_number_Set() const;
    bool is_number_Valid() const;

    qint32 getPar() const;
    void setPar(const qint32 &par);
    bool is_par_Set() const;
    bool is_par_Valid() const;

    qint32 getPars() const;
    void setPars(const qint32 &pars);
    bool is_pars_Set() const;
    bool is_pars_Valid() const;

    qint32 getPlayerRoundId() const;
    void setPlayerRoundId(const qint32 &player_round_id);
    bool is_player_round_id_Set() const;
    bool is_player_round_id_Valid() const;

    qint32 getPlayerTournamentId() const;
    void setPlayerTournamentId(const qint32 &player_tournament_id);
    bool is_player_tournament_id_Set() const;
    bool is_player_tournament_id_Valid() const;

    qint32 getScore() const;
    void setScore(const qint32 &score);
    bool is_score_Set() const;
    bool is_score_Valid() const;

    QString getTeeTime() const;
    void setTeeTime(const QString &tee_time);
    bool is_tee_time_Set() const;
    bool is_tee_time_Valid() const;

    qint32 getTripleBogeys() const;
    void setTripleBogeys(const qint32 &triple_bogeys);
    bool is_triple_bogeys_Set() const;
    bool is_triple_bogeys_Valid() const;

    qint32 getWorseThanDoubleBogey() const;
    void setWorseThanDoubleBogey(const qint32 &worse_than_double_bogey);
    bool is_worse_than_double_bogey_Set() const;
    bool is_worse_than_double_bogey_Valid() const;

    qint32 getWorseThanTripleBogey() const;
    void setWorseThanTripleBogey(const qint32 &worse_than_triple_bogey);
    bool is_worse_than_triple_bogey_Set() const;
    bool is_worse_than_triple_bogey_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_back_nine_start;
    bool m_back_nine_start_isSet;
    bool m_back_nine_start_isValid;

    qint32 m_birdies;
    bool m_birdies_isSet;
    bool m_birdies_isValid;

    bool m_bogey_free;
    bool m_bogey_free_isSet;
    bool m_bogey_free_isValid;

    qint32 m_bogeys;
    bool m_bogeys_isSet;
    bool m_bogeys_isValid;

    double m_bounce_back_count;
    bool m_bounce_back_count_isSet;
    bool m_bounce_back_count_isValid;

    double m_consecutive_birdie_or_better_count;
    bool m_consecutive_birdie_or_better_count_isSet;
    bool m_consecutive_birdie_or_better_count_isValid;

    QString m_day;
    bool m_day_isSet;
    bool m_day_isValid;

    qint32 m_double_bogeys;
    bool m_double_bogeys_isSet;
    bool m_double_bogeys_isValid;

    qint32 m_double_eagles;
    bool m_double_eagles_isSet;
    bool m_double_eagles_isValid;

    qint32 m_eagles;
    bool m_eagles_isSet;
    bool m_eagles_isValid;

    qint32 m_hole_in_ones;
    bool m_hole_in_ones_isSet;
    bool m_hole_in_ones_isValid;

    QList<OAIPlayerHole> m_holes;
    bool m_holes_isSet;
    bool m_holes_isValid;

    bool m_includes_five_or_more_birdies_or_better;
    bool m_includes_five_or_more_birdies_or_better_isSet;
    bool m_includes_five_or_more_birdies_or_better_isValid;

    bool m_includes_streak_of_five_birdies_or_better;
    bool m_includes_streak_of_five_birdies_or_better_isSet;
    bool m_includes_streak_of_five_birdies_or_better_isValid;

    bool m_includes_streak_of_four_birdies_or_better;
    bool m_includes_streak_of_four_birdies_or_better_isSet;
    bool m_includes_streak_of_four_birdies_or_better_isValid;

    bool m_includes_streak_of_six_birdies_or_better;
    bool m_includes_streak_of_six_birdies_or_better_isSet;
    bool m_includes_streak_of_six_birdies_or_better_isValid;

    bool m_includes_streak_of_three_birdies_or_better;
    bool m_includes_streak_of_three_birdies_or_better_isSet;
    bool m_includes_streak_of_three_birdies_or_better_isValid;

    double m_longest_birdie_or_better_streak;
    bool m_longest_birdie_or_better_streak_isSet;
    bool m_longest_birdie_or_better_streak_isValid;

    qint32 m_number;
    bool m_number_isSet;
    bool m_number_isValid;

    qint32 m_par;
    bool m_par_isSet;
    bool m_par_isValid;

    qint32 m_pars;
    bool m_pars_isSet;
    bool m_pars_isValid;

    qint32 m_player_round_id;
    bool m_player_round_id_isSet;
    bool m_player_round_id_isValid;

    qint32 m_player_tournament_id;
    bool m_player_tournament_id_isSet;
    bool m_player_tournament_id_isValid;

    qint32 m_score;
    bool m_score_isSet;
    bool m_score_isValid;

    QString m_tee_time;
    bool m_tee_time_isSet;
    bool m_tee_time_isValid;

    qint32 m_triple_bogeys;
    bool m_triple_bogeys_isSet;
    bool m_triple_bogeys_isValid;

    qint32 m_worse_than_double_bogey;
    bool m_worse_than_double_bogey_isSet;
    bool m_worse_than_double_bogey_isValid;

    qint32 m_worse_than_triple_bogey;
    bool m_worse_than_triple_bogey_isSet;
    bool m_worse_than_triple_bogey_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPlayerRound)

#endif // OAIPlayerRound_H

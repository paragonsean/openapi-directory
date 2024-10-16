/**
 * shinobiapi
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIRatingItem.h
 *
 * 
 */

#ifndef OAIRatingItem_H
#define OAIRatingItem_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIRatingItem : public OAIObject {
public:
    OAIRatingItem();
    OAIRatingItem(QString json);
    ~OAIRatingItem() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getEpisoDate() const;
    void setEpisoDate(const QString &episo_date);
    bool is_episo_date_Set() const;
    bool is_episo_date_Valid() const;

    QString getImdb() const;
    void setImdb(const QString &imdb);
    bool is_imdb_Set() const;
    bool is_imdb_Valid() const;

    QString getMetaCritics() const;
    void setMetaCritics(const QString &meta_critics);
    bool is_meta_critics_Set() const;
    bool is_meta_critics_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getRottenTomatoes() const;
    void setRottenTomatoes(const QString &rotten_tomatoes);
    bool is_rotten_tomatoes_Set() const;
    bool is_rotten_tomatoes_Valid() const;

    QString getRottenTomatoesAudienceScore() const;
    void setRottenTomatoesAudienceScore(const QString &rotten_tomatoes_audience_score);
    bool is_rotten_tomatoes_audience_score_Set() const;
    bool is_rotten_tomatoes_audience_score_Valid() const;

    QString getTvdb() const;
    void setTvdb(const QString &tvdb);
    bool is_tvdb_Set() const;
    bool is_tvdb_Valid() const;

    QString getTvMaze() const;
    void setTvMaze(const QString &tv_maze);
    bool is_tv_maze_Set() const;
    bool is_tv_maze_Valid() const;

    QString getTrakt() const;
    void setTrakt(const QString &trakt);
    bool is_trakt_Set() const;
    bool is_trakt_Valid() const;

    QString getImdbId() const;
    void setImdbId(const QString &imdb_id);
    bool is_imdb_id_Set() const;
    bool is_imdb_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_episo_date;
    bool m_episo_date_isSet;
    bool m_episo_date_isValid;

    QString m_imdb;
    bool m_imdb_isSet;
    bool m_imdb_isValid;

    QString m_meta_critics;
    bool m_meta_critics_isSet;
    bool m_meta_critics_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_rotten_tomatoes;
    bool m_rotten_tomatoes_isSet;
    bool m_rotten_tomatoes_isValid;

    QString m_rotten_tomatoes_audience_score;
    bool m_rotten_tomatoes_audience_score_isSet;
    bool m_rotten_tomatoes_audience_score_isValid;

    QString m_tvdb;
    bool m_tvdb_isSet;
    bool m_tvdb_isValid;

    QString m_tv_maze;
    bool m_tv_maze_isSet;
    bool m_tv_maze_isValid;

    QString m_trakt;
    bool m_trakt_isSet;
    bool m_trakt_isValid;

    QString m_imdb_id;
    bool m_imdb_id_isSet;
    bool m_imdb_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIRatingItem)

#endif // OAIRatingItem_H

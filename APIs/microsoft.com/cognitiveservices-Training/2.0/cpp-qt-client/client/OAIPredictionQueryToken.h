/**
 * TrainingApi
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIPredictionQueryToken.h
 *
 * 
 */

#ifndef OAIPredictionQueryToken_H
#define OAIPredictionQueryToken_H

#include <QJsonObject>

#include "OAIPredictionQueryTag.h"
#include <QDateTime>
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIPredictionQueryTag;

class OAIPredictionQueryToken : public OAIObject {
public:
    OAIPredictionQueryToken();
    OAIPredictionQueryToken(QString json);
    ~OAIPredictionQueryToken() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getApplication() const;
    void setApplication(const QString &application);
    bool is_application_Set() const;
    bool is_application_Valid() const;

    QString getContinuation() const;
    void setContinuation(const QString &continuation);
    bool is_continuation_Set() const;
    bool is_continuation_Valid() const;

    QDateTime getEndTime() const;
    void setEndTime(const QDateTime &end_time);
    bool is_end_time_Set() const;
    bool is_end_time_Valid() const;

    QString getIterationId() const;
    void setIterationId(const QString &iteration_id);
    bool is_iteration_id_Set() const;
    bool is_iteration_id_Valid() const;

    qint32 getMaxCount() const;
    void setMaxCount(const qint32 &max_count);
    bool is_max_count_Set() const;
    bool is_max_count_Valid() const;

    QString getOrderBy() const;
    void setOrderBy(const QString &order_by);
    bool is_order_by_Set() const;
    bool is_order_by_Valid() const;

    QString getSession() const;
    void setSession(const QString &session);
    bool is_session_Set() const;
    bool is_session_Valid() const;

    QDateTime getStartTime() const;
    void setStartTime(const QDateTime &start_time);
    bool is_start_time_Set() const;
    bool is_start_time_Valid() const;

    QList<OAIPredictionQueryTag> getTags() const;
    void setTags(const QList<OAIPredictionQueryTag> &tags);
    bool is_tags_Set() const;
    bool is_tags_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_application;
    bool m_application_isSet;
    bool m_application_isValid;

    QString m_continuation;
    bool m_continuation_isSet;
    bool m_continuation_isValid;

    QDateTime m_end_time;
    bool m_end_time_isSet;
    bool m_end_time_isValid;

    QString m_iteration_id;
    bool m_iteration_id_isSet;
    bool m_iteration_id_isValid;

    qint32 m_max_count;
    bool m_max_count_isSet;
    bool m_max_count_isValid;

    QString m_order_by;
    bool m_order_by_isSet;
    bool m_order_by_isValid;

    QString m_session;
    bool m_session_isSet;
    bool m_session_isValid;

    QDateTime m_start_time;
    bool m_start_time_isSet;
    bool m_start_time_isValid;

    QList<OAIPredictionQueryTag> m_tags;
    bool m_tags_isSet;
    bool m_tags_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPredictionQueryToken)

#endif // OAIPredictionQueryToken_H

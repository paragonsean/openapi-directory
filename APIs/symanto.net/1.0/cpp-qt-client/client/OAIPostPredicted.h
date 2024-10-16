/**
 * Psycholinguistic Text Analytics
 * We aim to provide the deepest understanding of people through psychology & AI
 *
 * The version of the OpenAPI document: 1.0
 * Contact: support@symanto.net
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIPostPredicted.h
 *
 * 
 */

#ifndef OAIPostPredicted_H
#define OAIPostPredicted_H

#include <QJsonObject>

#include "OAIPrediction.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIPrediction;

class OAIPostPredicted : public OAIObject {
public:
    OAIPostPredicted();
    OAIPostPredicted(QString json);
    ~OAIPostPredicted() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QList<OAIPrediction> getPredictions() const;
    void setPredictions(const QList<OAIPrediction> &predictions);
    bool is_predictions_Set() const;
    bool is_predictions_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QList<OAIPrediction> m_predictions;
    bool m_predictions_isSet;
    bool m_predictions_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPostPredicted)

#endif // OAIPostPredicted_H

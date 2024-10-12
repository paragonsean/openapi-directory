/**
 * Spotify Web API with fixes and improvements from sonallux
 * You can use Spotify's Web API to discover music and podcasts, manage your Spotify library, control audio playback, and much more. Browse our available Web API endpoints using the sidebar at left, or via the navigation bar on top of this page on smaller screens.  In order to make successful Web API requests your app will need a valid access token. One can be obtained through <a href=\"https://developer.spotify.com/documentation/general/guides/authorization-guide/\">OAuth 2.0</a>.  The base URI for all Web API requests is `https://api.spotify.com/v1`.  Need help? See our <a href=\"https://developer.spotify.com/documentation/web-api/guides/\">Web API guides</a> for more information, or visit the <a href=\"https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer\">Spotify for Developers community forum</a> to ask questions and connect with other developers. 
 *
 * The version of the OpenAPI document: 2023.2.27
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIAudioAnalysisObject_track.h
 *
 * 
 */

#ifndef OAIAudioAnalysisObject_track_H
#define OAIAudioAnalysisObject_track_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIAudioAnalysisObject_track : public OAIObject {
public:
    OAIAudioAnalysisObject_track();
    OAIAudioAnalysisObject_track(QString json);
    ~OAIAudioAnalysisObject_track() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getAnalysisChannels() const;
    void setAnalysisChannels(const qint32 &analysis_channels);
    bool is_analysis_channels_Set() const;
    bool is_analysis_channels_Valid() const;

    qint32 getAnalysisSampleRate() const;
    void setAnalysisSampleRate(const qint32 &analysis_sample_rate);
    bool is_analysis_sample_rate_Set() const;
    bool is_analysis_sample_rate_Valid() const;

    double getCodeVersion() const;
    void setCodeVersion(const double &code_version);
    bool is_code_version_Set() const;
    bool is_code_version_Valid() const;

    QString getCodestring() const;
    void setCodestring(const QString &codestring);
    bool is_codestring_Set() const;
    bool is_codestring_Valid() const;

    double getDuration() const;
    void setDuration(const double &duration);
    bool is_duration_Set() const;
    bool is_duration_Valid() const;

    double getEchoprintVersion() const;
    void setEchoprintVersion(const double &echoprint_version);
    bool is_echoprint_version_Set() const;
    bool is_echoprint_version_Valid() const;

    QString getEchoprintstring() const;
    void setEchoprintstring(const QString &echoprintstring);
    bool is_echoprintstring_Set() const;
    bool is_echoprintstring_Valid() const;

    double getEndOfFadeIn() const;
    void setEndOfFadeIn(const double &end_of_fade_in);
    bool is_end_of_fade_in_Set() const;
    bool is_end_of_fade_in_Valid() const;

    qint32 getKey() const;
    void setKey(const qint32 &key);
    bool is_key_Set() const;
    bool is_key_Valid() const;

    double getKeyConfidence() const;
    void setKeyConfidence(const double &key_confidence);
    bool is_key_confidence_Set() const;
    bool is_key_confidence_Valid() const;

    float getLoudness() const;
    void setLoudness(const float &loudness);
    bool is_loudness_Set() const;
    bool is_loudness_Valid() const;

    qint32 getMode() const;
    void setMode(const qint32 &mode);
    bool is_mode_Set() const;
    bool is_mode_Valid() const;

    double getModeConfidence() const;
    void setModeConfidence(const double &mode_confidence);
    bool is_mode_confidence_Set() const;
    bool is_mode_confidence_Valid() const;

    qint32 getNumSamples() const;
    void setNumSamples(const qint32 &num_samples);
    bool is_num_samples_Set() const;
    bool is_num_samples_Valid() const;

    qint32 getOffsetSeconds() const;
    void setOffsetSeconds(const qint32 &offset_seconds);
    bool is_offset_seconds_Set() const;
    bool is_offset_seconds_Valid() const;

    double getRhythmVersion() const;
    void setRhythmVersion(const double &rhythm_version);
    bool is_rhythm_version_Set() const;
    bool is_rhythm_version_Valid() const;

    QString getRhythmstring() const;
    void setRhythmstring(const QString &rhythmstring);
    bool is_rhythmstring_Set() const;
    bool is_rhythmstring_Valid() const;

    QString getSampleMd5() const;
    void setSampleMd5(const QString &sample_md5);
    bool is_sample_md5_Set() const;
    bool is_sample_md5_Valid() const;

    double getStartOfFadeOut() const;
    void setStartOfFadeOut(const double &start_of_fade_out);
    bool is_start_of_fade_out_Set() const;
    bool is_start_of_fade_out_Valid() const;

    double getSynchVersion() const;
    void setSynchVersion(const double &synch_version);
    bool is_synch_version_Set() const;
    bool is_synch_version_Valid() const;

    QString getSynchstring() const;
    void setSynchstring(const QString &synchstring);
    bool is_synchstring_Set() const;
    bool is_synchstring_Valid() const;

    float getTempo() const;
    void setTempo(const float &tempo);
    bool is_tempo_Set() const;
    bool is_tempo_Valid() const;

    double getTempoConfidence() const;
    void setTempoConfidence(const double &tempo_confidence);
    bool is_tempo_confidence_Set() const;
    bool is_tempo_confidence_Valid() const;

    qint32 getTimeSignature() const;
    void setTimeSignature(const qint32 &time_signature);
    bool is_time_signature_Set() const;
    bool is_time_signature_Valid() const;

    double getTimeSignatureConfidence() const;
    void setTimeSignatureConfidence(const double &time_signature_confidence);
    bool is_time_signature_confidence_Set() const;
    bool is_time_signature_confidence_Valid() const;

    qint32 getWindowSeconds() const;
    void setWindowSeconds(const qint32 &window_seconds);
    bool is_window_seconds_Set() const;
    bool is_window_seconds_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_analysis_channels;
    bool m_analysis_channels_isSet;
    bool m_analysis_channels_isValid;

    qint32 m_analysis_sample_rate;
    bool m_analysis_sample_rate_isSet;
    bool m_analysis_sample_rate_isValid;

    double m_code_version;
    bool m_code_version_isSet;
    bool m_code_version_isValid;

    QString m_codestring;
    bool m_codestring_isSet;
    bool m_codestring_isValid;

    double m_duration;
    bool m_duration_isSet;
    bool m_duration_isValid;

    double m_echoprint_version;
    bool m_echoprint_version_isSet;
    bool m_echoprint_version_isValid;

    QString m_echoprintstring;
    bool m_echoprintstring_isSet;
    bool m_echoprintstring_isValid;

    double m_end_of_fade_in;
    bool m_end_of_fade_in_isSet;
    bool m_end_of_fade_in_isValid;

    qint32 m_key;
    bool m_key_isSet;
    bool m_key_isValid;

    double m_key_confidence;
    bool m_key_confidence_isSet;
    bool m_key_confidence_isValid;

    float m_loudness;
    bool m_loudness_isSet;
    bool m_loudness_isValid;

    qint32 m_mode;
    bool m_mode_isSet;
    bool m_mode_isValid;

    double m_mode_confidence;
    bool m_mode_confidence_isSet;
    bool m_mode_confidence_isValid;

    qint32 m_num_samples;
    bool m_num_samples_isSet;
    bool m_num_samples_isValid;

    qint32 m_offset_seconds;
    bool m_offset_seconds_isSet;
    bool m_offset_seconds_isValid;

    double m_rhythm_version;
    bool m_rhythm_version_isSet;
    bool m_rhythm_version_isValid;

    QString m_rhythmstring;
    bool m_rhythmstring_isSet;
    bool m_rhythmstring_isValid;

    QString m_sample_md5;
    bool m_sample_md5_isSet;
    bool m_sample_md5_isValid;

    double m_start_of_fade_out;
    bool m_start_of_fade_out_isSet;
    bool m_start_of_fade_out_isValid;

    double m_synch_version;
    bool m_synch_version_isSet;
    bool m_synch_version_isValid;

    QString m_synchstring;
    bool m_synchstring_isSet;
    bool m_synchstring_isValid;

    float m_tempo;
    bool m_tempo_isSet;
    bool m_tempo_isValid;

    double m_tempo_confidence;
    bool m_tempo_confidence_isSet;
    bool m_tempo_confidence_isValid;

    qint32 m_time_signature;
    bool m_time_signature_isSet;
    bool m_time_signature_isValid;

    double m_time_signature_confidence;
    bool m_time_signature_confidence_isSet;
    bool m_time_signature_confidence_isValid;

    qint32 m_window_seconds;
    bool m_window_seconds_isSet;
    bool m_window_seconds_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAudioAnalysisObject_track)

#endif // OAIAudioAnalysisObject_track_H

package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"sort"
)

type Data struct {
	NextOffset int    `json:"next_offset"`
	List       []Song `json:"list"`
}

type Song struct {
	ID               string    `json:"rec_id"`
	POI              string    `json:"poi"`
	Key              string    `json:"key"`
	PerformanceKey   string    `json:"performance_key"`
	JoinLink         string    `json:"join_link"`
	Type             string    `json"type"`
	Title            string    `json:"title"`
	Artist           string    `json:"artist"`
	Message          string    `json:"message"`
	CreatedAt        string    `json:"created_at"`
	ExpiredAt        string    `json:"expire_at"`
	Seed             bool      `json:"seed"`
	Closed           bool      `json:"closed"`
	EnsembleType     string    `json:"ensemble_type"`
	ChildCount       int       `json:"child_count"`
	AppUID           string    `json:"app_uid"`
	ArrType          string    `json:"arr_type"`
	SongID           string    `json:"song_id"`
	SongLength       string    `json:"song_length"`
	PerfStatus       string    `json:"perft_status"`
	ArtistTwitter    string    `json:"artist_twitter"`
	MediaURL         string    `json:"media_url"`
	VideoMediaURL    string    `json:"video_media_url"`
	VideoMediaMp4URL string    `json:"video_media_mp4_url"`
	CoverURL         string    `json:"cover_url"`
	WebURL           string    `json:"web_url"`
	SongInfoURL      string    `json:"song_info_url"`
	Stats            Statistic `json:"stats"`
	Year             int       `json:"year"`
	ImdbID           string    `json:"imdbID"`
	PerformedBy      string    `json:"performed_by"`
	PerformedByURL   string    `json:"performed_by_url"`
	Owner            User      `json:"owner"`
	OtherPerformers  []User    `json:"other_performers"`
	Duet             string    `json:"duet"`
	Other            string    `json:"other"`
	Featured         bool      `json:"featured"`
	Rm               string    `json:"rm"`
	Private          string    `json:"private"`
	LyricVideo       string    `json:"lyric_video"`
	Lyrics           string    `json:"lyrics"`
	Segments         string    `json:"segments"`
}

type Statistic struct {
	TotalPerformers          int    `json:"total_performers"`
	TruncatedOtherPerformers string `json:"truncated_other_performers"`
	TotalListens             int    `json:"total_listens"`
	TruncatedListens         string `json:"truncated_listens"`
	TotalLoves               int    `json:"total_loves"`
	TruncatedLoves           string `json:"truncated_loves"`
	TotalComments            int    `json:"total_comments"`
	TruncatedComments        string `json:"truncated_comments"`
	TotalCommenters          int    `json"total_commenters"`
	TotalGifts               int    `json:"total_gifts"`
	TruncatedGifts           string `json:"truncated_gifts"`
}

type User struct {
	AccountID    int     `json:"account_id"`
	Handle       string  `json:"handle"`
	PicURL       string  `json:"pic_url"`
	Price        float32 `json"price"`
	Discount     float32 `json"discount"`
	URL          string  `json:"url"`
	IsVIP        bool    `json:"is_vip"`
	IsVerified   bool    `json:"is_verified"`
	VerifiedType string  `json:"verified_type"`
}

func main() {
	resp, err := http.Get("https://www.smule.com/bnrmusic/performances/json")
	if err != nil {
		log.Fatalln(err)
	}
	defer resp.Body.Close()
	var DataStruct Data
	decoder := json.NewDecoder(resp.Body)
	if err := decoder.Decode(&DataStruct); err != nil {
		fmt.Println("ooopsss! an error occurred, please try again")
	}
	arr := []string{}
	for _, element := range DataStruct.List {
		arr = append(arr, element.Title)
	}
	// for DataStruct.NextOffset != -1 {
	// 	resp, err := http.Get("https://www.smule.com/bnrmusic/performances/json?offset=" + DataStruct.NextOffset)
	// 	if err != nil {
	// 		log.Fatalln(err)
	// 	}
	// 	defer resp.Body.Close()
	// 	var NestedDataStruct Data
	// 	decoder = json.NewDecoder(resp.Body)
	// 	err = decoder.Decode(&NestedDataStruct)
	// 	if err != nil {
	// 		fmt.Println(err)
	// 	}
	// 	for _, element := range NestedDataStruct.Data {
	// 		arr = append(arr, element.Title)
	// 	}
	// }
	sort.Slice(arr, func(i, j int) bool {
		return arr[i] < arr[j]
	})
	for _, element := range arr {
		fmt.Println(element)
	}
}

import googleapiclient.discovery
import googleapiclient.errors

# Function to get comments from a YouTube video (with pagination)
def get_video_comments(video_id, api_key):
    # Build the YouTube API client
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)

    # List to hold all comments
    comments = []
    next_page_token = None

    try:
        while True:
            # Make the API request
            request = youtube.commentThreads().list(
                part="snippet",
                videoId=video_id,
                textFormat="plainText",
                maxResults=100,  # Max number of comments per request
                pageToken=next_page_token  # Pagination logic
            )
            response = request.execute()

            # Check if comments are returned
            if 'items' in response:
                for item in response['items']:
                    comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
                    comments.append(comment)

            # Check if there is another page of comments
            next_page_token = response.get('nextPageToken')

            # Break if there are no more comments to fetch
            if not next_page_token:
                break

            print(f"Fetched {len(comments)} comments so far...")  # Debugging output

        print(f"Total comments fetched: {len(comments)}")  # Final debug output
    except googleapiclient.errors.HttpError as e:
        print(f"Error occurred: {e}")
    
    return comments

# Function to save comments to a text file
def save_comments_to_file(comments, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            for comment in comments:
                f.write(comment + '\n')
        print(f"Comments saved to {filename}")  # Debugging output
    except Exception as e:
        print(f"Error saving comments: {e}")

# Main script logic
def main():
    # Get user input for API key and video ID
    api_key = input("Enter your YouTube API Key: ")  # Prompt for API key
    video_id = input("Enter the YouTube video ID: ")  # Prompt for Video ID

    print(f"Fetching comments for video ID: {video_id}")  # Debugging output
    
    comments = get_video_comments(video_id, api_key)

    if comments:
        save_comments_to_file(comments, 'youtube_comments.txt')
    else:
        print("No comments to save.")

if __name__ == "__main__":
    main()

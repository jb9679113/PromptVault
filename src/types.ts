export interface PromptItem {
  id: string;
  title: string;
  description: string;
  content: string;
  tags: string[];
  isFavorite: boolean;
  createdAt: string;
  updatedAt: string;
}

export interface FilterState {
  searchTerm: string;
  selectedTag: string | null;
  showFavoritesOnly: boolean;
}
